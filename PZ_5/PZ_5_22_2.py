"""
Описать функцию Mean(X, Y, AMean, GMean), вычисляющую среднее  арифметическое AMean = (X+Y)/2 и среднее геометрическое
GMean = y/X Y двух  положительных чисел X и Y (X и Y — входные, AMean и GMean — выходные  параметры вещественного типа).
С помощью этой функции найти среднее  арифметическое
и среднее геометрическое для пар (A, B), (A, C), (A, D), если даны  A, B, C, D. python
"""
import random
import math


def mean(X, Y):
    AMean = (X + Y) / 2
    GMean = math.sqrt(X * Y)
    return AMean, GMean


numbers = [random.randrange(0, 10) for i in range(4)]
for j in range(1, 4):
    AMean, GMean = mean(numbers[0], numbers[j])
    print(f"(A, {['B', 'C', 'D'][j-1]})")
    print('AMean = ', AMean)
    print('GMean = ', GMean)
