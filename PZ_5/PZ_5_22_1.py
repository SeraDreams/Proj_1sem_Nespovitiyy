# Найти сумму чисел ряда 1,2,3,...,60 с использованием функции нахождения суммы.
# Использовать локальные переменные

def find_sum():
    # Инициализация переменных
    total = 0
    current_number = 1

    # Цикл для суммирования чисел
    while current_number <= 60:
        total += current_number
        current_number += 1

    return total


if __name__ == '__main__':
    # Вызов функции и вывод результата
    result = find_sum()
    print("Сумма чисел ряда 1, 2, 3, ..., 60 равна:", result)

