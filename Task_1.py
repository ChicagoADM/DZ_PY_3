# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции
import os
clear = lambda: os.system('cls')
clear()
import math
from random import Random, randint

arr = []
sum = 0

for i in range(10):
    arr.append(randint(1, 99))
    if i % 2 != 0:
        sum += arr[i]
print(f"Список из нескольких чисел {arr}")
print()
print(f"Сумму элементов списка, стоящих на нечётной позиции = {sum}")
print()
input('Нажмите Enter для выхода ...')