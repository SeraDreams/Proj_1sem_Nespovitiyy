"""
Из предложенного текстового файла (text18-22.txt) вывести на экран его содержимое,
количество букв в верхнем регистре. Сформировать новый файл, в который поместить текст
в стихотворной форме предварительно заменив символы третей строки их числовыми
кодами.
"""


def main():
    with open("assets/text18-22.txt", 'r', encoding='utf-16') as file:
        count_upper = 0
        fileread = file.read()
        print(fileread)
        for i in fileread.replace(' ', ''):
            if i == i.upper() and i.isalpha():
                count_upper += 1
        print(f"\nКоличество букв в верхнем регистре: {count_upper}")

        new_text = ""
        for char in fileread.split('\n')[2]:
            new_text += str(ord(char)) + ' '

        # Запись нового текста в файл
        with open('new_text.txt', 'w') as files:
            for c, i in enumerate(fileread.split('\n')):
                if c == 2:
                    files.write(new_text + '\n')
                else:
                    files.write(fileread.split('\n')[c] + '\n')


if __name__ == '__main__':
    main()
