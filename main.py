import telebot

bot = telebot.TeleBot('8690908197:AAHHahqwr5pE4ZQ7FT_ZQ50Zbzy6z6q3a60')

@bot.message_handler(commands=['start', 'hello'])
def start_hello(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}, я пока ничего не умею но клянусь научусь!')

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, '<b>Меню помощи</b>', parse_mode='html')

@bot.message_handler(func=lambda m: m.text and m.text.lower() in ['привет', 'id'])
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}, я пока ничего не умею но клянусь научусь!')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')

bot.polling(none_stop=True)