# 1. Создайте программу для игры с конфетами человек против компьютера.
# Условие задачи: На столе лежит 150 конфет. Играют игрок против компьютера. Первый
# ход определяется жеребьёвкой.За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Подумайте как наделить бота ""интеллектом""

from random import randint

def player_input(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите правильное количество конфет от 1 до 28: "))
    return x


def after_turn(name, k, counter, value):
    print(f"Ходил игрок {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")


def bot_ai(value):
    k = randint(1,29)
    while value-k <= 28 and value > 29:
        k = randint(1,29)
    return k

player1 = input("Введите имя игрока: ")
player2 = "Bot"
sweets = 150
turn = randint(0, 2)
if turn:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter_sweets1 = 0
counter_sweets2 = 0

while sweets > 28:
    if turn:
        k = player_input(player1)
        counter_sweets1 += k
        sweets -= k
        turn = False
        after_turn(player1, k, counter_sweets1, sweets)
    else:
        k = bot_ai(sweets)
        counter_sweets2 += k
        sweets -= k
        turn = True
        after_turn(player2, k, counter_sweets2, sweets)

if turn:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")