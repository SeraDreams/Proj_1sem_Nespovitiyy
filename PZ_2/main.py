def error():
    main(input('Пожалуйста! Введите трёхзначное число: '))


def main(number):
    if len(number) == 3 and number.isdigit():
        print(f'Первая цифра вашего числа: {int(number)//100}')
    else:
        error()


if __name__ == '__main__':
    main(input('Введите трёхзначное число: '))

