# Вариант 22
# 2

def main():
    try:
        a = float(input("Введите число A > 1: "))
        while not a > 1:
            a = float(input("Число A должно быть A > 1: "))
    except ValueError:
        print('ОШИБКА! ТРЕБУЕТСЯ ВЕСТИ ДАННЫЕ ПОВТОРНО!')
        main()

    k = 0
    temp = 0
    while temp <= a:
        k += 1
        temp = temp + 1 / k
    k -= 1
    temp -= 1 / k
    print("Наибольшее целое число K:", k)
    print("Сумма 1 + 1/2 + ... + 1/K:", temp)


if __name__ == '__main__':
    main()
