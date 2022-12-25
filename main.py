import telebot
from random import randint
import random

bot_name = 'Бот'

bot = telebot.TeleBot("TOKEN")

def correct_move(message) -> bool:

    """Функция проверяет корректность ввода в процессе игры"""

    global play_game

    if play_game == False:

        return False

    if 1 <= int(message.text) <= 28:

        return True

    else:

        bot.send_message(message.chat.id,f'\n{player}, некорректный ввод!\n')

        return False

@bot.message_handler(commands=['start'])
def start_message(message) -> str:

    """Функция выводит приветствие игрока"""

    player = message.from_user.first_name

    bot.send_message(message.chat.id,f'\nПривет, {player}, я {bot_name}! Давай сыграем в игру? Пришли команду /play, чтобы начать!\n')

@bot.message_handler(commands=['play'])
def start_game(message) -> str:

    """Функция запускает игру и выбирает того, кто сделает первых ход"""

    global candys, player, play_game

    player = message.from_user.first_name
    play_game = True
    candys = 117

    who_move = random.choice([True, False])

    bot.send_message(message.chat.id,f'\nНа столе {candys} конфет =) Брать за один раз можно не больше 28 конфет!!\n')

    if who_move == True:

        bot.send_message(message.chat.id,f'\nПервым ходит {player}.\n')

    else:

        bot.send_message(message.chat.id,f'\nПервым ходит {bot_name}.\n')

        k = randint(1,29)

        candys -= k

        bot.send_message(message.chat.id,f'\n{bot_name} взял {k} конфет(ы). На столе осталось {candys}.\n')

@bot.message_handler(func=correct_move)
def move(message) -> str:

    """Функция реализует саму игру и определяет победителя"""

    global candys, player, play_game

    if candys > 28 and play_game == True:

        k = int(message.text)

        candys -= k

        bot.send_message(message.chat.id,f'\nНа столе осталось {candys} конфет(ы).\n')

        if candys > 28 and play_game == True:

            k = randint(1,29)

            candys -= k

            bot.send_message(message.chat.id,f'\n{bot_name} взял {k} конфет(ы). На столе осталось {candys}.\n')

            if candys <= 28 and play_game == True:

                bot.send_message(message.chat.id,f'\nПоздравляем, {player}, ты выиграл у бездушной машины!\n')

                play_game = False

                bot.send_message(message.chat.id,f'\n{player}, пришли команду /play, чтобы начать заново!\n')

        else:

            bot.send_message(message.chat.id,f'\n{bot_name} обыграл человека!\n')

            play_game = False

            bot.send_message(message.chat.id,f'\n{player}, пришли команду /play, чтобы начать заново!\n')

    else: 

        bot.send_message(message.chat.id,f'\nПоздравляем, {player}, ты выиграл у бездушной машины!\n')

        play_game = False

        bot.send_message(message.chat.id,f'\n{player}, пришли команду /play, чтобы начать заново!\n')

print('Telegram bot server is in running state...')

bot.infinity_polling()