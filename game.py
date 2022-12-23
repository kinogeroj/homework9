import os
from random import randint

os.system('cls')

def input_dat(player_name) -> int:
    
    """Функция возвращает количество конфет, взятое игроком"""
 
    x = int(input(f'{player_name}, введите количество конфет, которое Вы возьмете (от 1 до 28): '))
    
    while x < 1 or x > 28:
        x = int(input(f'{player_name}, введите корректное количество конфет: '))

    os.system('cls')
    
    return x

def print_status(player_name, k, counter, candys) -> str:

    """Функция обновляет данные игры для игроков"""

    print(f'Ходил игрок {player_name}, взял {k} конфет, теперь у него {counter} конфет. На столе осталось {candys} конфет.')

player_one_name = input('Введите имя игрока: ')
player_two_name = 'Bot'

os.system('cls')

who_move = randint(0,2)

if who_move:
    print(f'Первым ходит {player_one_name}.')

else:
    print(f'Первым ходит {player_two_name}.')

counter1 = 0 
counter2 = 0

while candys > 28:

    if who_move:
        k = input_dat(player_one_name)
        counter1 += k
        global candys -= k
        who_move = False
        print_status (player_one_name, k, counter1, candys)

    else:
        os.system('cls')
        k = randint(1,29)
        counter2 += k
        candys -= k
        who_move = True
        print_status (player_two_name, k, counter2, candys)

if who_move:

    print('\nПоздравляем, ' + player_one_name + ', Вы выиграли!')

else:
    print('\n' + player_two_name + ' обыграл человека!')