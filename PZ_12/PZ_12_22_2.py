"""
2.Из заданной строки отобразить только символы пунктуации. Использовать
библиотеку string.
Строка: --msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}"
"""
import string

line = '--msg-template="$FileDir$\\{path}:{line}:{column}:{C}:({symbol}){msg}"'
punctuation_symbols = [char for char in line if char in string.punctuation]
punctuation_line = ''.join(punctuation_symbols)
print(f"Изначальные данные: {line}")
print(f"Символы пунктуации из строки: {punctuation_line}")
