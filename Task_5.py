# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
import os
clear = lambda: os.system('cls')
clear()
def Fibonacci(n):
    if n in [1, 2]:                       
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

def NegaFibonacci(n):
    if n == 1:                       
        return 1
    elif n == 2:                       
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, n):
            num1, num2 = num2, num1 - num2
        return num2

list = [0]
userNumber = int(input('Введите число: '))
for e in range(1, userNumber + 1):
    list.append(Fibonacci(e))
    list.insert(0, NegaFibonacci(e))
print(f'Cписок чисел Фибоначчи:\n{list}')
print()
input('Нажмите Enter для выхода ...')