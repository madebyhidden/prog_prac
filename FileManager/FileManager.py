import os
import shutil
import sys

import time

print("Добрый день. Выберите то, что Вас интересует")
time.sleep(0.7)
print("1. Создание папки (с указанием имени);\n"
      "2. Удаление папки по имени;\n"
      "3. Перемещение между папками (в пределах рабочей папки) - заход в папку по имени, выход на уровень вверх;\n"
      "4. Создание пустых файлов с указанием имени;\n"
      "5. Запись текста в файл;\n"
      "6. Просмотр содержимого текстового файла;\n"
      "7. Удаление файлов по имени;\n"
      "8. Копирование файлов из одной папки в другую;\n"
      "9. Перемещение файлов;\n"
      "10. Переименование файлов.\n"
      )

ch_dir = str("/home/FADOMAIN/213737/PycharmProjects/pythonProject")
print(ch_dir)
choise_fir = int(input("Введите цифру: "))


while True:

    os.chdir(ch_dir)
    if choise_fir == 1:
        print("Текущая папка: ", ch_dir)
        print("Для начала укажите имя папки: ")
        name_dir = input()
        if name_dir == str("exit"):
            print("")
        path_dir = ch_dir + "/" + name_dir

        os.mkdir(path_dir)

    if choise_fir == 2:
        print("Существующие папки в катологе\n", os.listdir(ch_dir))
        print("Для начала укажите имя папки: ")
        name_dir = str(input())

        if name_dir == str("exit"):
            print("")
        path_dir = ch_dir + "/" + name_dir
        shutil.rmtree(path_dir)
    if choise_fir == 3:

        print("Существующие папки в катологе\n", os.listdir(ch_dir))
        print("Впишите папку для перехода: ")
        dir_ch = input()
        while dir_ch != "exit":

            d_list = os.listdir(ch_dir)

            if dir_ch in d_list:
                print("Вы в папке", dir_ch)

                ch_dir = ch_dir + "/" + dir_ch + "/"

                print(ch_dir)
                print("Существующие папки в катологе\n", os.listdir(ch_dir))
                print("Впишите папку для перехода или exit: ")
                dir_ch = str(input())
                if dir_ch == "exit":
                    print("")
            else:
                print("Такой папки нет")

    if choise_fir == 4:
        print("Текущий каталог: ", ch_dir)
        print("Для начала укажите имя папки: ")
        choise_tri = str(input()) + ".txt"
        my_file = open(choise_tri, "w+")
        my_file.close()
    if choise_fir == 5:
        print("Существующие файлы в катологе\n", os.listdir(ch_dir))
        print("Для начала укажите имя файла: ")
        choise_tri = str(input()) + ".txt"
        my_file = open(choise_tri, "w+")
        print("Введите нужный текст : ")
        text_in = str(input())
        my_file.write(text_in)
        my_file.close()

    if choise_fir == 6:
        print("Существующие файлы в катологе\n", os.listdir(ch_dir))
        print("Для начала укажите имя файла: ")
        choise_tri = str(input()) + ".txt"
        my_file = open(choise_tri, "r+")
        file_contents = my_file.read()
        print(file_contents)
    if choise_fir == 7:
        print("hi")
    if choise_fir == 8:
        print("hi")
    if choise_fir == 9:
        print("hi")
    if choise_fir == 10:
        sys.exit()

    print("Желаете выйти?")
    print("1. Да\n"
          "2. Нет\n")
    choise_sec = int(input())
    if choise_sec == 1:
        sys.exit()
    if choise_sec == 2:
        print("Выберите то, что Вас интересует")
        time.sleep(0.7)
        print("1. Создание папки (с указанием имени);\n"
              "2. Удаление папки по имени;\n"
              "3. Перемещение между папками (в пределах рабочей папки) - заход в папку по имени, выход на уровень вверх;\n"
              "4. Создание пустых файлов с указанием имени;\n"
              "5. Запись текста в файл;\n"
              "6. Просмотр содержимого текстового файла;\n"
              "7. Удаление файлов по имени;\n"
              "8. Копирование файлов из одной папки в другую;\n"
              "9. Перемещение файлов;\n"
              "10. Переименование файлов.\n"
              )
        choise_fir = int(input("Введите цифру: "))