"""
Даны списки A и B одинакового размера N. Поменять местами их содержимое и
вывести вначале элементы преобразованного списка A, а затем — элементы
преобразованного списка B.
"""

import random

N = random.randrange(2, 11)
a, b = [[random.randrange(1, 10) for i in range(N)] for _ in range(2)]
print(f"N: {N}\nArray a:\n{a}\nArray b:\n{b}\n")
for i in range(0, N):
    a[i], b[i] = b[i], a[i]
print(f"N: {N}\nArray a:\n{a}\nArray b:\n{b}\n")
