import telebot
from textt import names
bot = telebot.TeleBot("7769174544:AAH5KGSpeV4_FIgxN39JPHhy6kvGVugE_Nw")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привіт, я телеграм-бот, який на основі прізвища виводить ім'я одногрупника.")
    bot.send_message(message.chat.id, "Напиши прізвище одногрупника.")


@bot.message_handler()
def name(message):
    first_name = message.text.lower()
    second_name = names.get(first_name, "Це не твій одногрупник.")
    bot.send_message(message.chat.id, second_name)


bot.polling()
