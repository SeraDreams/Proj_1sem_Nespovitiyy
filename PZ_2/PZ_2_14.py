def error():
    #пофторный опрос пользователя на число если оно было введено
    main(input('Пожалуйста! Введите трёхзначное число: '))


def main(number):
    #проверка вёл ли пользователь трёхзначное число
    if len(number) == 3 and number.isdigit():
        #вывод
        print(f'Первая цифра вашего числа: {int(number)//100}')
    else:
        error()


if __name__ == '__main__':
    #запрос у пользователя числа и его передача в функцию main
    main(input('Введите трёхзначное число: '))