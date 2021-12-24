import telebot
from telebot import types

# токен для pyTelegramBotAPI
token = "5006457026:AAGi7BBD_eBpQIHuRaWAL4HBWrw8KhaUFzg"

# объект бота
bot = telebot.TeleBot(token)


# Создаем команду старт и основные кнопки
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/help", "/abitur", "/faculties", "/MTUCI")
    bot.send_message(message.chat.id,
                     'Привет, это бот МТУСИ!\n '
                     'Нажми /help, чтобы узнать о возможностях бота', reply_markup=keyboard)


# Создание команды /help
@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'У бота есть ряд возможностей: \n\n'
                                      'Напиши "новости", узнать новости МТУСИ\n\n'
                                      'Напиши "эиос", чтобы попасть на ЭИОС МТУСИ\n\n'
                                      'Напиши "контакты", чтобы получить контакты, для связи с руководством МТУСИ\n\n'
                                      '/abitur - сайт приемной комисии\n\n'
                                      '/faculties - узнать о факультетах МТУСИ\n\n'
                                      '/MTUCI - узнать информацию о МТУСИ \n\n'
                                      '\n')


# Создание команды /abitur
@bot.message_handler(commands=['abitur'])
def start_message(message):
    bot.send_message(message.chat.id, '[Сайт приемной комиссии](https://abitur.mtuci.ru/', parse_mode='Markdown')


# Создание команды /faculties
@bot.message_handler(commands=['faculties'])
def start_message2(message):
    # создаю инлайн клавиатуру (внутри чата)
    keyboard2 = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(text='Информационные технологии', callback_data='IT')
    keyboard2.add(key1)
    key2 = types.InlineKeyboardButton(text='Кибернетика и информационная безопасность', callback_data='Cybernetics')
    keyboard2.add(key2)
    key3 = types.InlineKeyboardButton(text='Сети и системы связи', callback_data='Networks')
    keyboard2.add(key3)
    key4 = types.InlineKeyboardButton(text='Радио и телевидение', callback_data='Radio')
    keyboard2.add(key4)
    key5 = types.InlineKeyboardButton(text='Цифровая экономика и массовые коммуникации', callback_data='Economics')
    keyboard2.add(key5)
    bot.send_message(message.chat.id, 'Выбери интересующий факультет:\n', reply_markup=keyboard2)


# Создание команды /MTUCI
@bot.message_handler(commands=['MTUCI'])
def start_message(message):
    bot.send_message(message.chat.id, 'МТУСИ является ведущим отраслевым российским университетом в области '
                                      'телекоммуникаций, информационных технологий и информационной безопасности. '
                                      'Выпускники МТУСИ работают в ведущих российских и международных '
                                      'телекоммуникационных и ИТ-компаниях, таких как Ростелеком,'
                                      ' МТС, Мегафон, Яндекс, Фирма «1С», HP, Cisco Systems, Nokia, '
                                      'Лаборатория Касперского, ВГТРК, ТТЦ «Останкино»,и др. '
                                      'Факультет «Информационных технологии» МТУСИ входит в '
                                      'ТОП-10 IT факультетов вузов Москвы по версии Headhunter.')


# создаем декоратор отвечающий за ответ на текстовые сообщения
@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "новости":
        bot.send_message(message.chat.id, 'Новости МТУСИ: https://mtuci.ru/about_the_university/news/')
    if message.text.lower() == "эиос":
        bot.send_message(message.chat.id, 'ЭИОС: https://lms.mtuci.ru')
    if message.text.lower() == "контакты":
        bot.send_message(message.chat.id, 'Email mtuci@mtuci.ru\n\n'
                                          'Корпус на Авиамоторной улице:\n'
                                          'Номер телефона: +7 (495) 957-79-17\n\n'
                                          'Корпус на Народного ополчения:\n'
                                          'Номер телефона: +7 (495) 957-8482')

# данные к которым обращается инлайн клавиатура
@bot.callback_query_handler(func=lambda call: True)
def otvet(call):
    if call.data == 'IT':
        bot.send_message(call.message.chat.id, "Факультет «Информационные технологии» готовит профессионалов "
                                               "по приоритетным направлениям в IT-области "
                                               "по 4 направлениям подготовки бакалавриата (5 профилей), "
                                               "а также по программам магистратуры (3 магистерских программы). "
                                               "На факультете насчитывается 47 учебных групп, что составляет более "
                                               "1000 "
                                               "студентов, "
                                               "из них:  945 чел. на программах бакалавриата,  "
                                               "75 чел. на программах магистратуры.\n\n"
                                               "Узнать больше информации: "
                                               "https://mtuci.ru/about_the_university/departments/304/")

    elif call.data == 'Cybernetics':
        bot.send_message(call.message.chat.id, 'Факультет «Кибернетика и информационная безопасность» (КиИБ) '
                                               'готовит профессионалов по приоритетным направлениям в сфере '
                                               'интеллектуальных '
                                               'киберсистем и информационной безопасности по '
                                               '5 направлениям подготовки бакалавриата '
                                               'и специалитета (7 профилей и 2 специализации) и '
                                               '3 направлениям подготовки магистратуры (5 магистерских программ).\n\n'
                                               'Узнать больше информации: '
                                               'https://mtuci.ru/about_the_university/departments/2444/')
    elif call.data == 'Networks':
        bot.send_message(call.message.chat.id, 'Факультет «Сети и системы связи» (СиСС) был образован путем слияния '
                                               'двух факультетов («Автоматической электросвязи» - АЭС и '
                                               '«Многоканальной электросвязи» - МЭС) в 2004 году. История же создания '
                                               'факультета ведется с момента основания университета, т.е. с 1921 '
                                               'года, когда была начата подготовка специалистов в области телефонной '
                                               'и телеграфной связи.\n\n '
                                               'Узнать больше информации: '
                                               'https://mtuci.ru/about_the_university/departments/306/')

    elif call.data == 'Radio':
        bot.send_message(call.message.chat.id, 'Подготовка радиоинженеров началась в Московском электротехническом '
                                               'институте связи с момента открытия института (в 1921 году был проведен '
                                               'первый набор на радиотелеграфную специальность). Обучение на '
                                               'факультете '
                                               'проводит высококвалифицированный педагогический коллектив, в составе '
                                               'которого академики, доктора наук, широко известные как в нашей стране, '
                                               'так и за ее пределами. Многие из них являются не только известными '
                                               'учеными, '
                                               'но и разработчиками государственных стандартов, учебников и '
                                               'учебных пособий, по которым обучаются '
                                               'студенты в более чем 60 вузах РФ и стран СНГ.\n\n'
                                               'Узнать больше информации: '
                                               'https://mtuci.ru/about_the_university/departments/305/')


    elif call.data == 'Economics':
        bot.send_message(call.message.chat.id, 'Факультет осуществляет подготовку бакалавров и магистров '
                                               'по учебным планам, отражающим современные тенденции в теории '
                                               'и практике цифровой экономики, управления, бизнес-технологий, '
                                               'рекламы, бизнес-информатики, с учетом требований '
                                               'федеральных государственных образовательных стандартов высшего '
                                               'образования (ФГОС ВО) к подготовке кадров\n\n'
                                               'Узнать больше информации: '
                                               'https://mtuci.ru/about_the_university/departments/307/')



bot.infinity_polling()
