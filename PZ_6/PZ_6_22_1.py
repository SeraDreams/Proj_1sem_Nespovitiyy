"""
 Дан список размера N и целые числа K и L (1 < K ≤ L ≤ N). Найти среднее
 арифметическое всех элементов списка, кроме элементов с номерами от K до L
 включительно
"""

import random


N = random.randint(10, 20)
L = random.randrange(1, N)
K = random.randint(1, L)

print(f"N = {N}\nL = {L}\nK = {K}")
A = [random.randrange(1, 20) for i in range(N)]
print(f"Initial: {A}")
A1 = [j for i, j in enumerate(A) if i not in range(K, L + 1)]
print(f"\n{A1}\nSum = {sum(A1)}\nCount = {len(A1)}\nAverage = {int(sum(A1))/int(len(A1))}")
