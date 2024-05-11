import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('officeexpenses.db')
cursor = conn.cursor()

# Создание таблицы "Канцелярия", если она не существует
cursor.execute('DROP TABLE IF EXISTS OfficeExpenses')
cursor.execute('''CREATE TABLE IF NOT EXISTS OfficeExpenses
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
                fullname TEXT NOT NULL,
                department TEXT NOT NULL,
                expensetype TEXT NOT NULL,
                amount REAL NOT NULL)''')


# Функция для ввода данных в БД
def insertdata(fullname, department, expensetype, amount):
    cursor.execute('''INSERT INTO OfficeExpenses (fullname, department, expensetype, amount)
                  VALUES (?, ?, ?, ?)''', (fullname, department, expensetype, amount))
    conn.commit()
    print("Данные успешно добавлены в БД")


# Функции для поиска данных в БД
def searchdatabyfullname(fullname):
    cursor.execute('''SELECT * FROM OfficeExpenses WHERE fullname = ?''', (fullname,))
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("Данные не найдены")


def searchdatabydepartment(department):
    cursor.execute('''SELECT * FROM OfficeExpenses WHERE department = ?''', (department,))
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("Данные не найдены")


# Функции для удаления данных из БД
def deletedatabyid(id):
    cursor.execute('''DELETE FROM OfficeExpenses WHERE id = ?''', (id,))
    conn.commit()
    print("Данные успешно удалены из БД")


def deletedatabyexpensetype(expensetype):
    cursor.execute('''DELETE FROM OfficeExpenses WHERE expensetype = ?''', (expensetype,))
    conn.commit()
    print("Данные успешно удалены из БД")


# Функции для редактирования данных в БД
def updateamountbyid(id, newamount):
    cursor.execute('''UPDATE OfficeExpenses SET amount = ? WHERE id = ?''', (newamount, id))
    conn.commit()
    print("Данные успешно обновлены")


def updateexpensetypebydepartment(department, newexpensetype):
    cursor.execute('''UPDATE OfficeExpenses SET expensetype = ? WHERE department = ?''', (newexpensetype, department))
    conn.commit()
    print("Данные успешно обновлены")


# Пример использования функций
insertdata("Иванов Иван", "Отдел кадров", "Ручки", 500.0)
searchdatabyfullname("Иванов Иван")
updateamountbyid(1, 700.0)
searchdatabyfullname("Иванов Иван")
deletedatabyexpensetype("Ручки")
searchdatabyfullname("Иванов Иван")


# Закрытие соединения с БД
conn.close()
