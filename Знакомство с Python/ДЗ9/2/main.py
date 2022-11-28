import telebot

bot=telebot.TeleBot('5816935308:AAEeJ0UHLqScP90nBMLRA3WVGAx5rov4J3c')

info = dict()
    
@bot.message_handler(commands=['start'])
def start (message):
    bot.send_message(message.chat.id, '/menu')

@bot.message_handler(commands=['menu'])
def menu (message):
    bot.send_message(message.chat.id, '/start\n/save\n/print\n/search')

@bot.message_handler(commands=['save'])
def sta (message):
    bot.send_message(message.chat.id, 'Введите фамилию')
    bot.register_next_step_handler(message,surname_)
def surname_(message):
    surname = message.text
    global info
    info['Фамилия'] = surname.title()
    bot.send_message(message.chat.id, 'Введите имя')
    bot.register_next_step_handler(message,name_)
def name_ (message):
    name = message.text
    info['Имя'] = name.title()
    bot.send_message(message.chat.id, 'Введите отчество')
    bot.register_next_step_handler(message,patronymic_)
def patronymic_ (message):
    patronymic = message.text
    info['Отчество'] = patronymic.title()
    bot.send_message(message.chat.id, 'Введите номер телефона')
    bot.register_next_step_handler(message,telephone)
def telephone (message):
    phone  = message.text
    info['Телефон'] = phone
    bot.send_message(message.chat.id, 'Введите примечание')
    bot.register_next_step_handler(message,comment_)
def comment_ (message):
    comment  = message.text
    info['Примечание'] = comment
    with open('Phonebook_1.txt', 'a', encoding='utf-16') as file:
        file.write(f'{info}\n')

    with open('Phonebook_2.txt', 'a', encoding='utf-16') as file:
        for i,j in info.items():
            file.writelines(f'{i}: {j}\n')
        file.writelines(f'________________\n')
    bot.send_message(message.chat.id, 'Контакт добавлен')
    bot.send_message(message.chat.id, '/start\n/save\n/print\n/search')

@bot.message_handler(commands=['print'])
def print (message):
    bot.send_message(message.chat.id, 'Какую книгу показать (1 или 2)?')
    bot.register_next_step_handler(message,book_)
def book_(message):
    book = message.text
    if book == '1':
        with open('Phonebook_1.txt', 'r', encoding='utf-16') as file:
            for data in file:
                bot.send_message(message.chat.id, data)
    else:
        with open('Phonebook_2.txt', 'r', encoding='utf-16') as file:
            for data in file:
                bot.send_message(message.chat.id, data)
    bot.send_message(message.chat.id, '/start\n/save\n/print')

@bot.message_handler(commands=['search'])
def search (message):
    bot.send_message(message.chat.id, 'В какой книге искать (1 или 2)?')
    bot.register_next_step_handler(message,book_)
def book_(message):
    book = message.text
    if book == '1':
        bot.send_message(message.chat.id, 'Что искать:')
        bot.register_next_step_handler(message, print1)
    else:
        bot.send_message(message.chat.id, 'Что искать:')
        # bot.register_next_step_handler(message, print2)
def print1 (message):
    x = message.text
    with open('Phonebook_1.txt', 'r', encoding='utf-16') as file:
        for data in file:
            if x.lower() in data.lower():               
                bot.send_message(message.chat.id, data)
    bot.send_message(message.chat.id, '/start\n/save\n/print\n/search')           
# def print2 (message):
#     x = message.text    
#     with open('Phonebook_2.txt', 'r', encoding='utf-16') as file:
#         for data in file:
#             temp = ''
#             if data != '________________\n':
#                 temp += data.lower()
#             elif x in temp:
#                 bot.send_message(message.chat.id, temp)
#                 temp = ''
#             else:
#                 temp = ''
#     bot.send_message(message.chat.id, '/start\n/save\n/print\n/search')

bot.polling(none_stop=True, interval=0)