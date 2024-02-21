"""
1. В матрице найти минимальный элемент в предпоследнем столбце.
"""
import random


def generate_matrix(rows, columns, min_value, max_value):
    """
    Генератор матрицы.

    :param rows: Количество строк в матрице.
    :param columns: Количество столбцов в матрице.
    :param min_value: Минимальное значение элемента матрицы.
    :param max_value: Максимальное значение элемента матрицы.
    :return: Сгенерированная матрица.
    """
    matrix = [[random.randint(min_value, max_value) for _ in range(columns)] for _ in range(rows)]
    return matrix


def min_value_matrix(matrix):
    # Получаем количество столбцов в матрице
    num_columns = len(matrix[0])
    # Индекс предпоследнего столбца
    prelast_column_index = num_columns - 2
    # Получаем значения в предпоследнем столбце
    prelast_column_values = [row[prelast_column_index] for row in matrix]
    # Находим минимальное значение в предпоследнем столбце
    min_value = min(prelast_column_values)
    print("Минимальный элемент в предпоследнем столбце:", min_value)


if __name__ == '__main__':
    # Пример использования генератора
    rows = 5
    columns = 5
    min_value = 1
    max_value = 10

    matrix = generate_matrix(rows, columns, min_value, max_value)
    # Вывод сгенерированной матрицы
    print("Матрица:")
    for row in matrix:
        print(row)

    # Находим и выводим минимальное значение в предпоследнем столбце
    min_value_matrix(matrix)
