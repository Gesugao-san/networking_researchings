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

# Диалоговое окно для выбора файла
def open_file():
    file_types = [("Text Files", "*.txt"), ("All Files", "*.*")]
    path = filedialog.askopenfilename(filetypes=file_types)
    if path:
        text_widget.delete(1.0, tk.END)  # Очищаем текстовое поле
        with open(path, "r") as file:
            lines = file.readlines()

        category_name = "/////// nothing"  # Устанавливаем значение по умолчанию
        for line in lines:
            line = line.strip()
            if line.startswith("///////"):
                category_name = line
            elif line.startswith("//"):
                text_widget.insert(tk.END, f"{line}\n")
            elif line:
                text_widget.insert(tk.END, f"{category_name}\n{line}\n")

# Кнопка для выбора файла
open_button = tk.Button(root, text="Выбрать файл", command=open_file)
open_button.pack()

# Запускаем главный цикл приложения
root.mainloop()







