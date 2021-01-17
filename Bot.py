import telebot

import config

bot = telebot.TeleBot(config.token)

keyboard = telebot.types.ReplyKeyboardMarkup(True)
keyboard.row('привет', 'здорова', 'здравствуйте')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, config.fisrt_phrase,
                     reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def send_answer(message):
    pharases = config.pharases
    if message.text.lower() in pharases:
        bot.send_message(message.chat.id, config.hello)
    else:
        bot.send_message(message.chat.id, config.i_dont_know)


bot.polling()
