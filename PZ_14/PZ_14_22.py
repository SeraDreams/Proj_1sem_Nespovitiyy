"""
Из исходного текстового файла (ip_address.txt) из раздела «Частоупотребимые
маски» перенести в первый файл строки с нулевым четвертым октетом, а во второй
– все остальные. Посчитать количество полученных строк в каждом файле.
"""
import re


def find_text(text):
    """
    Args:
      text: Текст, в котором нужно найти текст.
      start_marker: Начало поиска
      end_marker: Конец поиска

    Returns:
      Строка с найденным текстом.
    """
    start_marker = "Частоупотребимые маски"
    end_marker = "Количество адресов подсети не равно количеству возможных узлов. Нулевой IP-адрес резервируется для идентификации подсети, последний — в качестве широковещательного адреса. Таким образом, в реально действующих сетях возможно количество узлов на два меньшее количества адресов."

    start_index = text.find(start_marker)
    if start_index == -1:
        return None

    end_index = text.find(end_marker, start_index + len(start_marker))
    if end_index == -1:
        return None

    return text[start_index + len(start_marker):end_index]


with open("records/ip_address.txt", "r") as input_file, \
        open("records/first_file.txt", "w") as first_output_file, \
        open("records/second_file.txt", "w") as second_output_file:
    for line in find_text(input_file.read()).split('\n'):
        # Проверка четвертого октета
        if re.match(r".*\.0$", line):
            first_output_file.write(line + '\n')
        elif not line in ' ':
            second_output_file.write(line + '\n')

# Подсчет строк
first_file_lines = sum(1 for line in open("records/first_file.txt"))
second_file_lines = sum(1 for line in open("records/second_file.txt"))

print("Внутреннее содержание файла first_file.txt:", open("records/first_file.txt").read().split())
print(f"Количество строк в first_file.txt: {first_file_lines}\n")
print("Внутреннее содержание файла second_file.txt:", open("records/second_file.txt").read().split())
print(f"Количество строк в second_file.txt: {second_file_lines}\n")
