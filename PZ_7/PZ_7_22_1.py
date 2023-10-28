def calculate_digit_sum():
    try:
        number = input("Введите целое положительное число: ")
        while not number.isdigit() and not int(number) >= 0:
            number = input("Введите целое положительное число: ")

        digit_sum = 0
        for digit_char in number:
            digit = int(digit_char)
            digit_sum += digit

        print("Сумма цифр числа:", digit_sum)
    except:
        print('ОШИБКА! ТРЕБУЕТСЯ ВЕСТИ ДАННЫЕ ПОВТОРНО!')
        calculate_digit_sum()


if __name__ == '__main__':
    calculate_digit_sum()
