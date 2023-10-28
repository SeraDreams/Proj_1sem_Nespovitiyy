"""
Дано множество A из N точек (точки заданы своими координатами х, у). Среди всех
точек этого множества, лежащих во второй четверти, найти точку, наиболее
удаленную от начала координат. Если таких точек нет, то вывести точку с нулевыми
координатами.
"""

import math


def find_farthest_point(points):
    farthest_point = (0, 0)
    max_distance = 0

    for point in points:
        x, y = point

        # Проверяем, что точка лежит во второй четверти
        if x < 0 and y > 0:
            distance = math.sqrt(x**2 + y**2)

            # Обновляем наибольшее расстояние и точку
            if distance > max_distance:
                max_distance = distance
                farthest_point = point

    return farthest_point


# Пример использования функции
points = [(2, 3), (-1, 4), (-5, 2), (-3, -2), (0, 0), (-2, 1)]
farthest_point = find_farthest_point(points)

# Вывод результата
if farthest_point == (0, 0):
    print("Нет точек во второй четверти. Выводим точку с нулевыми координатами.")
else:
    print("Наиболее удаленная точка от начала координат во второй четверти:", farthest_point)
