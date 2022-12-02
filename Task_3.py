# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
import os
clear = lambda: os.system('cls')
clear()
import random
from random import Random, randint

num1 = randint(4, 9)
arr1 = []

for i in range(num1):
    num2 = random.uniform(1, 9)
    arr1.append(round(num2, 2))

num_max = arr1[0]
num_min = arr1[0]

for i in range(num1):
    if num_max < arr1[i]:
        num_max = arr1[i]
    if num_min > arr1[i]:
        num_min = arr1[i]

num_max -= int(num_max)
num_min -= int(num_min)

print(f'Cписок из вещественных чисел: {arr1}')

if num_max > num_min:
    sum = num_max - num_min
    print(f'Разницу между максимальным и минимальным значением дробной части элементов = {round(sum, 2)}')
    
elif num_max < num_min:
    sum = num_min - num_max
    print(f'Разницу между максимальным и минимальным значением дробной части элементов = {round(sum, 2)}')
print()
input('Нажмите Enter для выхода ...')