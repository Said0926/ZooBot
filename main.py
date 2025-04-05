import telebot, os, logging
from telebot import types
from config import API_TOKEN
from quiz import quiz_data, ANIMAL_RESULTS, welcome_text, help_text, about_text, support_text, feedback_text


bot = telebot.TeleBot(API_TOKEN)

# Настройки логирования
logging.basicConfig(
    filename='bot_errors.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)



# Словарь для хранения ответов пользователя
user_data = {}


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, welcome_text)


# Обработчик команды /help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, help_text)


# Обработчик команды /about
@bot.message_handler(commands=['about'])
def send_about(message):
    bot.reply_to(message, about_text)

# Обработчик команды /support
@bot.message_handler(commands=['support'])
def send_support(message):

    # Добавим кнопку для быстрого написания сообщения
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='Написать сообщение ✉️', url='https://moscowzoo.ru/contacts'))

    bot.reply_to(message, support_text, reply_markup=markup)



# Обработчик команды /feedback
@bot.message_handler(commands=['feedback'])
def send_feedback(message):
    # Добавим кнопку для быстрого написания отзыва
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text="Оставить отзыв ✍️", url="https://otzovik.com/reviews/moskovskiy_zoopark/"))

    bot.reply_to(message, feedback_text, reply_markup=markup)



# Обработчик команды /quiz
@bot.message_handler(commands=['quiz'])
def start_quiz(message):
    user_id = message.from_user.id
    user_data[user_id] = {
        'question_index': 0,
        'answers': [],
        'score': 0
    }
    ask_question(user_id, 0)


# Задаем вопрос
def ask_question(user_id, question_index):
    try:
        markup = create_markup(question_index)
        progress = get_progress(question_index)
        question_text = f"{progress}\n{quiz_data[question_index]['question']}"
        bot.send_message(user_id, question_text, reply_markup=markup)
    except Exception as e:
        logging.error(f'Ошибка в ask_question: {e}', exc_info=True)
        bot.send_message(user_id, "⚠️ Произошла ошибка при загрузке вопроса. Пожалуйста, попробуйте еще раз.")

# Создаем кнопки
def create_markup(question_index):
    markup = types.InlineKeyboardMarkup()
    for option in quiz_data[question_index]['options']:
        markup.add(types.InlineKeyboardButton(text=option, callback_data=option))
    return markup


# Оформление вопроса
def get_progress(question_index):
    total = len(quiz_data)
    return f"Вопрос {question_index + 1}/{total} [{'⭐' * (question_index + 1)}{'☆' * (total - question_index - 1)}]"



@bot.callback_query_handler(func=lambda call: True)
def handle_button_click(call):
    user_id = call.from_user.id
    if user_id not in user_data:
        bot.answer_callback_query(call.id, "Начните викторину через /quiz")
        return

    current_data = user_data[user_id]
    question_index = current_data['question_index']

    # Сохраняем ответ
    if call.data in quiz_data[question_index]['options']:
        answer_score = quiz_data[question_index]['scores'][
            quiz_data[question_index]['options'].index(call.data)
        ]
        current_data['answers'].append({
            'question': quiz_data[question_index]['question'],
            'answer': call.data,
            'score': answer_score
        })
        current_data['score'] += answer_score

    # Переход к следующему вопросу
    question_index += 1
    current_data['question_index'] = question_index

    if question_index < len(quiz_data):
        ask_question(user_id, question_index)
    else:
        # Генерируем результат
        result = generate_result(current_data['score'])
        send_result(user_id, result)
        del user_data[user_id]  # Очищаем данные

    bot.answer_callback_query(call.id, "✅ Ответ принят")


# Определяем какое животное подходит
def generate_result(total_score):
    try:
        if total_score >= 20:
            return ANIMAL_RESULTS["elephant"]
        elif total_score >= 17:
            return ANIMAL_RESULTS["eagle"]
        elif total_score >= 14:
            return ANIMAL_RESULTS["tiger"]
        elif total_score >= 11:
            return ANIMAL_RESULTS["lion"]
        elif total_score >= 8:
            return ANIMAL_RESULTS["kangaroo"]
        elif total_score >= 5:
            return ANIMAL_RESULTS["dolphin"]
        else:
            return ANIMAL_RESULTS["panda"]
    except Exception as e:
        logging.error(f'Ошибка в generate_result: {e}', exc_info=True)
        return {
            'text' : "⚠️ Произошла ошибка при определении результата. Пожалуйста, попробуйте еще раз.",
        }


# Отправляем результат
def send_result(user_id, result):
    try:
        image_path = os.path.join("images", result["image"])
        with open(image_path, 'rb') as photo:
            # Создаем клавиатуру с кнопками для share
            markup = types.InlineKeyboardMarkup(row_width=2)
            markup.add(
                types.InlineKeyboardButton(text='Поделиться в Telegram 📤', url=f'https://t.me/share/url?url={result['text']}'),
                types.InlineKeyboardButton(text='Поделиться ВКонтакте 🌐', url=f"https://vk.com/share.php?title={result['text']}")
            )
            markup.add(types.InlineKeyboardButton(text='Начать заново 🔄', callback_data='quiz'))

            # Отправляем результат с кнопками
            bot.send_photo(
                user_id,
                photo,
                caption=(
                    f"{result['text']}\n\n"
                    f"Ваш результат: {user_data[user_id]['score']} баллов!\n\n"
                    "Спасибо за прохождение викторины! 🐾\n"
                    "Поделись результатом с друзьями и предложи им тоже узнать, какое животное им подходит!\n\n"
                    "Поделитесь результатом с друзьями! 🐾"
                ),
                reply_markup=markup
            )
    except FileNotFoundError:
        bot.send_message(
            user_id,
            (
                f"{result['text']}\n\n"
                f"Ваш результат: {user_data[user_id]['score']} баллов!\n\n"
                "⚠️ Изображение не найдено, но мы уже работаем над этим!\n\n"
                "Чтобы начать заново, нажми /quiz."
            ),
            reply_markup=markup
        )
    except Exception as e:
        logging.error(f'Ошибка в send_result: {e}', exc_info=True)
        bot.send_message(user_id, "⚠️ Произошла ошибка при отправке результата. Пожалуйста, попробуйте еще раз. /quiz")




# Глобальный обработчик ошибок для callback_query
@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    try:
        handle_button_click(call)
    except Exception as e:
        logging.error(f'Ошибка в callback_query: {e}', exc_info=True)
        bot.answer_callback_query(call.id, "⚠️ Произошла ошибка. Пожалуйста, попробуйте еще раз.")


# Обработчик ошибок несуществующих команд
@bot.message_handler(func=lambda message: True)
def handle_unknown(message):
    bot.reply_to(
        message,
        "Извините, я не понимаю эту команду. 😅\n"
        "Попробуйте /help, чтобы узнать, как я могу вам помочь!"
    )



if __name__ == '__main__':
    if not os.path.exists("images"):
        os.makedirs("images")
    bot.polling(non_stop=True)