import telebot

import config

bot = telebot.TeleBot(config.token)

keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard.row(*config.phrases_first_button)
keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard2.row(config.phrases_second_button)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, config.phrases['word after start'],
                     reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def send_answer(message):
    if message.text.lower() in config.phrases_first_button:
        bot.send_message(message.chat.id, config.phrases['say hello'])
        bot.send_message(message.chat.id, config.phrases['ask me about strong'],
                         reply_markup=keyboard2)
    elif message.text.lower() == config.phrases_second_button:
        bot.send_message(message.chat.id, config.phrases['I know where strong'])
        bot.send_message(message.chat.id,
                         config.phrases['More questions'])
    else:
        bot.send_message(message.chat.id, config.phrases['i do not know'])


bot.polling()
