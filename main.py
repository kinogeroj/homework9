import telebot
from random import randint
import random

bot = telebot.TeleBot("5964599176:AAFMY94KAXcOdBx1d-Xfi_XMMUWq468HyMg")

bot_name = 'Бот'

def correct_move(message):

    if 1 <= int(message.text) <= 28:

        return True

    else:

        return False

@bot.message_handler(commands=['start'])

def start_message(message):
    
    bot.send_message(message.chat.id,f'Привет, {message.from_user.first_name}, я {bot_name}! Давай сыграем в игру? Пришли команду /play, чтобы начать!\n')

@bot.message_handler(commands=['play'])

def start_game(message):

    global candys, who_move, player

    player = message.from_user.first_name
    candys = 117
    
    who_move = random.choice([True, False])

    bot.send_message(message.chat.id,f'На столе {candys} конфет =) Брать за один раз можно не больше 28 конфет!!\n')

    if who_move == True:
        
        bot.send_message(message.chat.id,f'Первым ходит {player}.\n')
    
    else:

        bot.send_message(message.chat.id,f'Первым ходит {bot_name}.\n')

    while candys > 28:
            
        if who_move == True:
                
            @bot.message_handler(func=correct_move)
                
            def move(message):
                    
                global candys, who_move

                k = int(message.text)
                    
                candys -= k

                who_move = False

        else:

            k = randint(1,29)
        
            candys -= k
        
            who_move = True
        
            bot.send_message(message.chat.id,f'{bot_name} взял {k} конфет(ы). На столе осталось {candys}.\n')

    if who_move == True:

        bot.send_message(message.chat.id,f'\nПоздравляем, {player}, ты выиграл у бездушной машины!\n')

    else:
        
        bot.send_message(message.chat.id,f'\n {bot_name} обыграл человека!')

    bot.send_message(message.chat.id,f'\n{player}, пришли команду /play, чтобы начать заново!\n')

print('Telegram bot server is in running state...')

bot.infinity_polling()