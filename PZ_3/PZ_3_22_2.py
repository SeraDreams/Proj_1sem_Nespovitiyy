# Вариант 22.
# 2. Даны два числа. Вывести большее из них.

def main(number_1, number_2):
    try:
        float(number_1)
        float(number_2)
        if number_1 > number_2:
            print("Большее число:", number_1)
        elif number_2 > number_1:
            print("Большее число:", number_2)
        else:
            print("Числа равны")
    except:
        number_1 = input("ОШИБКА! Введите повторно первое число: ")
        number_2 = input("Введите повторно второе число: ")
        main(number_1, number_2)


if __name__ == '__main__':
    number_1 = input("Введите первое число: ")
    number_2 = input("Введите второе число: ")
    main(number_1, number_2)
