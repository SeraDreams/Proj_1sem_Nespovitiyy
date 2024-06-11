import os

pz6 = '/home/alexey/PycharmProjects/Proj_1sem_Nespovitiyy/PZ_6'
pz7 = '/home/alexey/PycharmProjects/Proj_1sem_Nespovitiyy/PZ_7'
pz11 = '/home/alexey/PycharmProjects/Proj_1sem_Nespovitiyy/PZ_11'
report = '/home/alexey/PycharmProjects/Proj_1sem_Nespovitiyy/Reports/'
p7_name = ''

# 1. Переход в каталог PZ11 и вывод списка файлов
os.chdir(pz11)
files = os.listdir()
for file in files:
    if not os.path.isdir(file):
        print(file)

# 2. Создание папок, перемещение файлов и вывод информации о размере
os.chdir("../")  # Переход в корень проекта
os.makedirs("test/test1", exist_ok=True)  # Создание папок
for c, file in enumerate(os.listdir(pz6), start=1):  # Перемещение двух файлов из ПЗ6
    if c <= 2:
        os.rename(pz6 + "/" + file, "test/" + file)
    else:
        break
for c, file in enumerate(os.listdir(pz7), start=1):  # Перемещение одного файла из ПЗ7
    if c <= 1:
        os.rename(pz7 + "/" + file, "test/test1/test.txt")
    else:
        break
file_sizes = [file + ': ' + str(os.path.getsize("test/" + file)) + ' byte' for file in os.listdir("test")]
print("Размеры файлов в папке test:", file_sizes)

# 3. Поиск файла с самым коротким именем в PZ11
# shortest_filename = [[int(len(str(i))), str(i)] for i in os.listdir(pz11)]
shortest_filename_2 = min([[len(os.path.basename(i)), os.path.basename(i)] for i in os.listdir(pz11)], key=lambda x: x[0])
print("Файл с самым коротким именем:", shortest_filename_2)

# 4. Запуск PDF-файла
# os.startfile(report + pdf_file)
os.system("evince /home/alexey/PycharmProjects/Proj_1sem_Nespovitiyy/Reports/PZ_17_22.pdf")

# 5. Удаление файла test.txt
with open('/home/alexey/PycharmProjects/Proj_1sem_Nespovitiyy/test/test1/test.txt', 'r') as file:
    print(file.read())
os.remove("/home/alexey/PycharmProjects/Proj_1sem_Nespovitiyy/test/test1/test.txt")
