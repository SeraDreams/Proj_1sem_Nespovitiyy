"""
Дана строка 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16', отражающая продажи продукции
по дням в кг. Преобразовать информацию из строки в словари, с использованием функции найти
максимальные продажи по каждому виду продукции, результаты вывести на экран.
"""

import re


string = 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16'
# Используем регулярное выражение для разбиения строки на слова и группы цифр
result = re.findall(r'\w+|\d+', string)
# Создаем словарь, где ключами являются слова, а значениями - списки групп цифр
sales_data = {}
selected_word = None
for element in result:
    if element.isalpha():
        selected_word = element
        sales_data[selected_word] = []
    else:
        sales_data[selected_word].append(int(element))

print(sales_data)
# Выводим результат
for word, numbers in sales_data.items():
    print('Полный словарь ', word, numbers)
    print('Максимальное кол-во продаж в кг ', word, max(numbers))
