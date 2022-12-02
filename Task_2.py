# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
import os
clear = lambda: os.system('cls')
clear()
from random import Random, randint
import math

num = randint(4, 8)
arr1 = []
arr2 = []
sum = 0

for i in range(num):
    arr1.append(randint(1, 10))

for i in range(math.ceil(num / 2)):
    sum = arr1[i] * arr1[(num - 1) - i]
    arr2.append(sum)
    
print(arr1)
print()
print(arr2)
print()
input('Нажмите Enter для выхода ...')