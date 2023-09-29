#!/usr/bin/env python3
# -*- coding: utf-8 -*-



import os
import tkinter as tk


# Создаем главное окно
root = tk.Tk()
root.title("Отображение значений из файла")

# Создаем текстовое поле для вывода значений
text_widget = tk.Text(root, height=40, width=120)
text_widget.pack()

# Открываем и читаем файл
with open(os.getcwd() + '\\p2p\\tixati\\l18n\\tixati_language_template.txt', "r") as file:
    lines = file.readlines()

category_name = ""
for line in lines:
    line = line.strip()

    #if line in ['\n', '\r\n']:
    #    continue

    if line.startswith("///////"):
        print('detected category:', line)
        category_name = line
    elif line.startswith("//"):
        print('detected comment:', line)
        category_name = line
    elif line:
        text_widget.insert(tk.END, f"{category_name}\n{line}\n")

# Запускаем главный цикл приложения
print('go')
root.mainloop()

