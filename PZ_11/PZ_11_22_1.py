"""
Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
последовательности из целых положительных и отрицательных чисел. Сформировать
новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
обработку элементов:

Содержимое первого файла:
Четные элементы:
Количество четных элементов:
Среднее арифметическое:

Содержимое второго файла:
Нечетные элементы:
Количество нечетных элементов:
Сумма положительных элементов:
"""

import random


def main():
    with open("plus.txt", 'w') as file:
        for i in range(10):
            file.write(f'{(random.randint(-50, 50))}\n')

    with open("minus.txt", 'w') as file:
        for i in range(10):
            file.write(f'{(random.randint(-50, 50))}\n')

    with open("plus.txt", 'r') as file:
        list_chet = []
        list = file.read().split()
        for i in list:
            if int(i) % 2 == 0:
                list_chet.append(int(i))
        with open('ready_plus.txt', 'w') as file_plus:
            file_plus.write(f'Содержимое первого файла: {[int(x) for x in list]}\n')
            file_plus.write(f"Чётные элементы: {list_chet}\n")
            file_plus.write(f"Кол-во чётных элементов: {len(list_chet)}\n")
            file_plus.write(f"Среднее арифметическое: {sum(list_chet)/len(list_chet)}")

        print(f'Содержимое первого файла: {[int(x) for x in list]}')
        print(f"Чётные элементы: {list_chet}")
        print(f"Кол-во чётных элементов: {len(list_chet)}")
        print(f"Среднее арифметическое: {sum(list_chet)/len(list_chet)}\n\n")

    with open("minus.txt", 'r') as file:
        list_nechet = []
        list = file.read().split()
        list_plus = []
        for i in list:
            if int(i) % 2 == 0:
                list_nechet.append(int(i))
            if int(i) >= 0:
                list_plus.append(int(i))
        with open("ready_minus.txt", 'w') as files_minus:
            files_minus.write(f'Содержимое второго файла: {[int(x) for x in list]}\n')
            files_minus.write(f"Нечётные элементы: {list_nechet}\n")
            files_minus.write(f"Кол-во нечётных элементов: {len(list_nechet)}\n")
            files_minus.write(f"Сумма положительных чисел: {sum(list_plus)}")

        print(f'Содержимое второго файла: {[int(x) for x in list]}')
        print(f"Нечётные элементы: {list_nechet}")
        print(f"Кол-во нечётных элементов: {len(list_nechet)}")
        print(f"Сумма положительных чисел: {sum(list_plus)}")


if __name__ == '__main__':
    main()
