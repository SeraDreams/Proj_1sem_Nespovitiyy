# Найти сумму чисел ряда 1,2,3,...,60 с использованием функции нахождения суммы.
# Использовать локальные переменные

def find_sum(num):
    # Инициализация переменных
    total = 0
    current_number = 1

    # Цикл для суммирования чисел
    while current_number <= num:
        total += current_number
        current_number += 1

    return total


if __name__ == '__main__':
    # Вызов функции и вывод результата
    num = 3
    result = find_sum(num=num)
    print("Сумма чисел ряда 1, 2, 3, ..., 60 равна:", result)

