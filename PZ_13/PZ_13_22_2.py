"""
2. Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее
элементов.
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


def average_of_odd_rows(matrix):
    """
    Найти среднее арифметическое элементов каждой строки матрицы с нечетным номером.

    :param matrix: Матрица.
    :return: Список средних арифметических значений для каждой строки с нечетным номером.
    """
    result = []
    for i in range(len(matrix)):
        if (i + 1) % 2 == 1:  # проверка на нечетность
            row_sum = sum(matrix[i])
            row_average = row_sum / len(matrix[i])
            print(f"Среднее арифметическое строки с нечетным номером {i+1}: {row_average}")
            result.append(row_average)
    return result


if __name__ == '__main__':
    # Пример использования
    rows = 4
    columns = 4
    min_value = 1
    max_value = 10

    matrix = generate_matrix(rows, columns, min_value, max_value)
    # Вывод сгенерированной матрицы
    print("Матрица:")
    for row in matrix:
        print(row)

    # Находим среднее арифметическое для каждой строки с нечетным номером
    average_of_odd_rows(matrix)
