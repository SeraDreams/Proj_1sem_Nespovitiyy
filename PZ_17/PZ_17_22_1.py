"""
. В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
приближенный к оригиналу (см. таблицу 1).
"""
import tkinter as tk
from tkinter import ttk


def create_form():
    root = tk.Tk()
    root.title("Форма регистрации пользователя")

    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    title = ttk.Label(frame, text="Форма регистрации пользователя", font=("Helvetica", 16))
    title.grid(row=0, column=0, columnspan=3, pady=10)

    ttk.Label(frame, text="Ваше имя:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
    name_entry = ttk.Entry(frame)
    name_entry.grid(row=1, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5)

    ttk.Label(frame, text="Пароль:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
    password_entry = ttk.Entry(frame, show="*")
    password_entry.grid(row=2, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5)

    ttk.Label(frame, text="Возраст:").grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
    age_entry = ttk.Entry(frame)
    age_entry.grid(row=3, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5)

    ttk.Label(frame, text="Пол:").grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)
    gender_var = tk.StringVar()
    ttk.Radiobutton(frame, text="Мужской", variable=gender_var, value="Мужской").grid(row=4, column=1, pady=5, sticky=tk.W)
    ttk.Radiobutton(frame, text="Женский", variable=gender_var, value="Женский").grid(row=4, column=2, pady=5, sticky=tk.W)

    ttk.Label(frame, text="Ваши увлечения:").grid(row=5, column=0, sticky=tk.W, padx=5, pady=5)
    hobbies_music = ttk.Checkbutton(frame, text="Музыка")
    hobbies_video = ttk.Checkbutton(frame, text="Видео")
    hobbies_drawing = ttk.Checkbutton(frame, text="Рисование")
    hobbies_music.grid(row=5, column=1, sticky=tk.W, pady=5)
    hobbies_video.grid(row=5, column=2, sticky=tk.W, pady=5)
    hobbies_drawing.grid(row=5, column=3, sticky=tk.W, pady=5)

    ttk.Label(frame, text="Ваша страна:").grid(row=6, column=0, sticky=tk.W, padx=5, pady=5)
    country_combobox = ttk.Combobox(frame)
    country_combobox['values'] = ("Россия", "США", "Китай", "Япония", "Германия")
    country_combobox.grid(row=6, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5)

    ttk.Label(frame, text="Ваш город:").grid(row=7, column=0, sticky=tk.W, padx=5, pady=5)
    city_combobox = ttk.Combobox(frame)
    city_combobox['values'] = ("Москва", "Нью-Йорк", "Пекин", "Токио", "Берлин")
    city_combobox.grid(row=7, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5)

    ttk.Label(frame, text="Кратко о себе:").grid(row=8, column=0, sticky=tk.W, padx=5, pady=5)
    short_info_text = tk.Text(frame, height=5, width=30)
    short_info_text.grid(row=8, column=1, columnspan=2, pady=5, sticky=(tk.W, tk.E))

    ttk.Label(frame, text="Решите пример, запишите результат в полe ниже:").grid(row=9, column=0, columnspan=3, sticky=tk.W, padx=5, pady=5)
    result_entry = ttk.Entry(frame)
    result_entry.grid(row=10, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)

    cancel_button = ttk.Button(frame, text="Отменить ввод")
    confirm_button = ttk.Button(frame, text="Данные подтверждаю")
    cancel_button.grid(row=11, column=0, pady=10)
    confirm_button.grid(row=11, column=2, pady=10)

    for widget in frame.winfo_children():
        widget.grid_configure(padx=5, pady=5)

    root.mainloop()


if __name__ == "__main__":
    create_form()

