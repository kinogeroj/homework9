import telebot
import game

bot = telebot.TeleBot("5964599176:AAFMY94KAXcOdBx1d-Xfi_XMMUWq468HyMg")

candys = 117

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    global candys
    candys -= int(message.text)
    bot.send_message(message.chat.id, str(candys))

bot.infinity_polling()