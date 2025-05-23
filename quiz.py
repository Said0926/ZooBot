quiz_data = [
    {
        'question' : 'Какой климат вам больше нравится?',
        'options' : ['Жаркий', 'Умеренный', 'Холодный'],
        'scores' : [5, 3, 1]
    },
    {
        'question' : 'Какой вид отдыха вы предпочитаете?',
        'options' : ['Активный', 'Спокойный', 'Экстремальный'],
        'scores' : [5, 2, 4]
    },
    {
        'question' : 'Какой размер животного вам больше нравится?',
        'options' : ['Маленький', 'Средний', 'Большой'],
        'scores' : [2, 4, 6]
    },
    {
        'question': 'Какую среду обитания вы считаете самой интересной?',
        'options': ['Лес', 'Горы', 'Водоемы', 'Пустыня'],
        'scores': [3, 5, 7, 2]
    }
]


ANIMAL_RESULTS = {
    "tiger": {
        "text": "🐅 Вам подходит тигр! Вы энергичны и любите приключения!",
        "image": "tiger.jpg"
    },
    "lion": {
        "text": "🦁 Ваш идеальный питомец - царь зверей лев! Вы прирожденный лидер!",
        "image": "lion.jpg"
    },
    "panda": {
        "text": "🐼 Милая панда - ваш лучший друг! Вы цените спокойствие и уют!",
        "image": "panda.jpg"
    },
    "eagle": {
        "text": "🦅 Вам подходит орел! Вы любите свободу и высоту!",
        "image": "eagle.jpg"
    },
    "dolphin": {
        "text": "🐬 Ваш идеальный питомец - дельфин! Вы общительны и любите воду!",
        "image": "dolphin.jpg"
    },
    "kangaroo": {
        "text": "🦘 Вам подходит кенгуру! Вы активны и полны энергии!",
        "image": "kangaroo.jpg"
    },
    "elephant": {
        "text": "🐘 Ваш идеальный питомец - слон! Вы мудры и спокойны!",
        "image": "elephant.jpg"
    }
}

welcome_text = (
        "Привет! 🐾 Добро пожаловать в бот Московского Зоопарка!\n\n"
        "Я помогу тебе узнать, какое животное подходит тебе больше всего. "
        "Для этого просто нажми /quiz и пройди увлекательную викторину!\n\n"
        "Также ты можешь узнать больше о командах бота, нажав /help.\n"
        "Давай начнем!"
    )

help_text = (
        "🦁 Список доступных команд:\n\n"
        "/start - Начать работу с ботом\n"
        "/quiz - Пройти викторину и узнать, какое животное тебе подходит\n"
        "/help - Посмотреть список команд\n"
        "/about - Узнать больше о боте\n"
        "/support - Связаться с поддержкой\n"
        "/feedback - Оставить отзыв или предложение\n\n"
        "Если у тебя есть вопросы или предложения, напиши нам!"
    )

about_text = (
        "🐼 О боте:\n\n"
        "Этот бот создан для того, чтобы помочь тебе узнать, какое животное из Московского Зоопарка "
        "подходит тебе по характеру и предпочтениям. Просто пройди викторину (/quiz), "
        "и я подскажу, кто твой идеальный питомец!\n\n"
        "Если у тебя есть вопросы или предложения, напиши нам:\n\n"
        "📞 Телефон: +7 (962) 971-38-75\n"
        "📧 Email: zoofriends@moscowzoo.ru\n"
        "💬 Telegram: @zoobot_support\n\n"
        "Спасибо, что используешь нашего бота! 🐾"
    )

support_text = (
        "🛠️ Нужна помощь? Мы всегда готовы помочь!\n\n"
        "Вы можете связаться с нами следующими способами:\n\n"
        "📞 Телефон: +7 (962) 971-38-75\n"
        "📧 Email: zoofriends@moscowzoo.ru\n"
        "💬 Telegram: @zoobot_support\n\n"
        "Если у вас есть вопрос или проблема, напишите нам, и мы обязательно ответим!\n\n"
        "Также вы можете отправить сообщение прямо здесь, и мы свяжемся с вами в ближайшее время."
    )

feedback_text = (
        "📣 Мы ценим ваше мнение!\n\n"
        "Если у вас есть отзыв, предложение или идея для улучшения бота, "
        "пожалуйста, напишите нам:\n\n"
        "📧 Email: feedback@zoobot.ru\n"
        "💬 Telegram: @zoobot_feedback\n\n"
        "Спасибо, что помогаете нам становиться лучше! ❤️"
    )