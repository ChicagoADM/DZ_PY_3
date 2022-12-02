# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
import os
clear = lambda: os.system('cls')
clear()
number = int(input('Введите число десятичное число: '))
print()
num = ''
while number > 0:
    num = str(number % 2) + num
    number //= 2
print(f'Двоичное число = {num}')
print()
input('Нажмите Enter для выхода ...')