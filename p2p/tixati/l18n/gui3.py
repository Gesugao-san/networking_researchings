#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import tkinter as tk
from tkinter import ttk
import json


path = os.getcwd() + '\\p2p\\tixati\\l18n\\data\\data1.json'


# Функция для чтения и отображения данных из JSON-файла
def load_data():
    try:
        with open(path, 'r') as file:
            data = json.load(file)
            text.delete(1.0, tk.END)
            text.insert(tk.END, json.dumps(data, indent=4))
    except FileNotFoundError:
        text.delete(1.0, tk.END)
        text.insert(tk.END, "Файл не найден.")

# Функция для сохранения отредактированных данных в JSON-файл
def save_data():
    try:
        updated_data = json.loads(text.get(1.0, tk.END))
        with open(path, 'w') as file:
            json.dump(updated_data, file, indent=4)
    except json.JSONDecodeError as e:
        text.delete(1.0, tk.END)
        text.insert(tk.END, f"Ошибка в JSON-формате: {e}")

# Создание главного окна
root = tk.Tk()
root.title("JSON Editor")

# Создание кнопок и текстового поля для отображения и редактирования данных
load_button = tk.Button(root, text="Загрузить данные", command=load_data)
load_button.pack()

save_button = tk.Button(root, text="Сохранить данные", command=save_data)
save_button.pack()

text = tk.Text(root, height=20, width=50)
text.pack()

# Запуск цикла событий tkinter
root.mainloop()





exit(0)

