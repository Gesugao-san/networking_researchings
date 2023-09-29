#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import filedialog
from tkinter import Scrollbar

# Создаем главное окно
root = tk.Tk()
root.title("Отображение значений из файла")

# Создаем текстовое поле для вывода значений
text_widget = tk.Text(root, height=40, width=120)
text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Добавляем полосу прокрутки
scrollbar = Scrollbar(root, command=text_widget.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_widget.config(yscrollcommand=scrollbar.set)

# Устанавливаем значение по умолчанию для category_name
category_name = "language window"

# Функция для открытия файла через диалоговое окно
def open_file_dialog():
    global category_name  # Сделаем category_name глобальной переменной
    file_types = [("Text Files", "*.txt"), ("All Files", "*.*")]
    path = filedialog.askopenfilename(filetypes=file_types)
    if path:
        text_widget.delete(1.0, tk.END)  # Очищаем текстовое поле
        with open(path, "r") as file:
            lines = file.readlines()
        parse_file(lines)

# Функция для разбора файла и вывода данных
def parse_file(lines):
    global category_name
    parsing_category = False
    line_num = -1
    for line in lines:
        line_num += 1
        line = line.strip()
        if line.startswith("///////"):
            category_name = line[len("/////// "):]  # Удаляем "/////// " из начала строки
            continue
        if not line:  # Пропускаем разделители — пустые строки
            continue
        elif line.startswith("//"):
            continue  # Игнорируем комментарии
        key = line
        value = lines.pop(line_num + 1).strip()  # Получаем следующую строку (Значение)
        data = [category_name, key, value]
        text_widget.insert(tk.END, f"{data}\n")  # Выводим Категорию, Ключ, Значение

# Кнопка для выбора файла через диалоговое окно
open_button = tk.Button(root, text="Выбрать файл", command=open_file_dialog)
open_button.pack()

# Запускаем главный цикл приложения
root.mainloop()
