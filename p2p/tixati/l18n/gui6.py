#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import tkinter as tk
from tkinter import ttk
import json

path = os.getcwd() + '\\p2p\\tixati\\l18n\\tixati_language_template.json'

# Функция для загрузки данных из JSON-файла и отображения их в таблице
def load_data():
    try:
        with open(path, 'r') as file:
            data = json.load(file)
            display_data(data)
    except FileNotFoundError:
        text.delete(1.0, tk.END)
        text.insert(tk.END, "Файл не найден.")

# Функция для отображения данных в виде вертикального текстового поля с прокруткой
def display_data(data):
    text.delete(1.0, tk.END)
    for record in data:
        for key, value in record.items():
            text.insert(tk.END, f"{key}: {value}\n")
        text.insert(tk.END, "\n")

# Функция для сохранения отредактированных данных в JSON-файл
def save_data():
    try:
        updated_data = []
        lines = text.get(1.0, tk.END).split('\n')
        record = {}
        for line in lines:
            line = line.strip()
            if line:
                key, value = line.split(':')
                record[key.strip()] = value.strip()
            else:
                if record:
                    updated_data.append(record)
                    record = {}
        with open(path, 'w') as file:
            json.dump(updated_data, file, indent=4)
    except Exception as e:
        text.delete(1.0, tk.END)
        text.insert(tk.END, f"Ошибка: {str(e)}")

# Создание главного окна
root = tk.Tk()
root.title("JSON Text Editor")

# Создание кнопок и текстового поля для отображения и редактирования данных
load_button = tk.Button(root, text="Загрузить данные", command=load_data)
load_button.pack()

save_button = tk.Button(root, text="Сохранить данные", command=save_data)
save_button.pack()

scrollbar = ttk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text = tk.Text(root, height=20, width=50, wrap=tk.WORD, yscrollcommand=scrollbar.set)
text.pack()

scrollbar.config(command=text.yview)

# Запуск цикла событий tkinter
root.mainloop()





exit(0)

