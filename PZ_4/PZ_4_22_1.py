# Вариант 22.
# 1
import math


def main():
    try:
        x = float(input("Введите вещественное число X: "))
        while not abs(x) < 1:
            x = float(input("Число X должно быть |X| < 1: "))

        n = int(input("Введите целое число N > 0: "))
        while not n > 0:
            n = int(input("Целое число N должно быть N > 0: "))

        a = x  # первый элемент последовательност иdouble
        suma = a  # Сумма элементов последовательности double
        eps = 0.00000001

        while abs(a) > eps:
            q = (((-1) * x * x ** (2 * n + 1)) / (2 * n + 3))
            a *= q  # Получаем следующий элемент последовательности
            suma += a  # Складываем все последующие элементы
            n += 1  # Увеличиваем счётчик

        print("Результат по данной формуле: ", suma)
        print("Результат от math: ", math.atan(x))

    except ValueError:
        print('ОШИБКА! ТРЕБУЕТСЯ ВЕСТИ ДАННЫЕ ПОВТОРНО!')
        main()


if __name__ == '__main__':
    main()