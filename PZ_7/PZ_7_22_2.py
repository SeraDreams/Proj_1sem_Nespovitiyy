def find_longest_word_length():
    try:
        sentence = str(input("Введите строку из русских слов: "))
        words = sentence.split()  # Разделение строки на слова
        longest_word_length = 0

        for word in words:
            word_length = len(word)
            if word_length > longest_word_length:
                longest_word_length = word_length

        length = longest_word_length
        # Вывод результата
        print("Длина самого длинного слова:", length)
    except:
        print('ОШИБКА! ТРЕБУЕТСЯ ВЕСТИ ДАННЫЕ ПОВТОРНО!')
        find_longest_word_length()


if __name__ == '__main__':
    find_longest_word_length()
