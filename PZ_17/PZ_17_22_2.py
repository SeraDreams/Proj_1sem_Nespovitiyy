"""
Разработать программу с применением пакета tk, взяв в качестве условия одну
любую задачу из ПЗ №№ 2 – 9.
ПЗ №2
Разработать программу, выводящую на экран первую цифру трёхзначного числа путём
использования одной операции деления нацело.
"""
import tkinter as tk


def validate_number(number_str):
  """
  Функция проверки, является ли введенное значение трехзначным числом.
  """
  if len(number_str.replace('-', '')) == 3 and number_str.replace('-', '').isdigit():
    return True
  else:
    return False


def get_first_digit(number):
  """
  Функция получения первой цифры из трехзначного числа.
  """
  return abs(int(number)) // 100


def show_result(number):
  """
  Функция отображения результата в окне Tkinter.
  """
  first_digit = get_first_digit(number)
  result_label.config(text=f"Первая цифра: {first_digit}")


def main():
  """
  Основная функция программы.
  """
  number_str = number_entry.get()
  if validate_number(number_str):
      show_result(number_str)
      error_label.config(text='')
  else:
      result_label.config(text='')
      error_label.config(text="Введите трёхзначное число!")


# Создание окна Tkinter
root = tk.Tk()
root.title("Первая цифра трёхзначного числа")

# Создание элементов интерфейса
number_label = tk.Label(root, text="Введите число:")
number_entry = tk.Entry(root)
result_label = tk.Label(root, text="")
error_label = tk.Label(root, text="", fg="red")
submit_button = tk.Button(root, text="Показать результат", command=main)

# Размещение элементов на окне
number_label.grid(row=0, column=0, sticky="w")
number_entry.grid(row=0, column=1)
result_label.grid(row=1, column=0, columnspan=2)
error_label.grid(row=2, column=0, columnspan=2)
submit_button.grid(row=3, column=0, columnspan=2)

# Запуск цикла обработки событий
root.mainloop()


if __name__ == "__main__":
  main()
