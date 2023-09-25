#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import tkinter as tk
from tkinter import ttk
import json
import pandas as pd

path = os.getcwd() + '\\p2p\\tixati\\l18n\\tixati_language_template.json'

# Глобальные переменные
dataframe = None
table = None

# Функция для загрузки данных из JSON-файла и отображения их в таблице
def load_data():
    global dataframe
    try:
        with open(path, 'r') as file:
            data = json.load(file)
            dataframe = pd.DataFrame(data)
            display_table(dataframe)
    except FileNotFoundError:
        dataframe = pd.DataFrame(columns=['Key', 'Value'])
        display_table(dataframe)

# Функция для отображения данных в виде таблицы
def display_table(df):
    global table
    for widget in frame.winfo_children():
        widget.destroy()

    table = ttk.Treeview(frame, columns=list(df.columns), show='headings')

    for col in df.columns:
        table.heading(col, text=col)
        table.column(col, width=100)

    for _, row in df.iterrows():
        table.insert("", "end", values=row.tolist())

    # Добавляем возможность редактирования ячеек
    for col in df.columns:
        table.bind('<Double-1>', edit_cell)

    table.pack(fill='both', expand=True)

# Функция для редактирования ячейки таблицы
def edit_cell(event):
    global table
    item = table.selection()
    if not item:
        return

    item = item[0]
    col = table.identify_column(event.x)

    col_id = col[1]
    col_name = table.heading(col_id)['text']

    # Создаем окно для редактирования значения
    edit_window = tk.Toplevel(root)
    edit_window.title("Редактирование")

    label = tk.Label(edit_window, text=f"Введите новое значение для {col_name}:")
    label.pack()

    edit_entry = tk.Entry(edit_window)
    edit_entry.pack()

    def save_edit():
        new_value = edit_entry.get()
        table.item(item, values=(table.item(item)['values'][0], new_value))
        dataframe.at[int(item), col_name] = new_value
        edit_window.destroy()

    save_button = tk.Button(edit_window, text="Сохранить", command=save_edit)
    save_button.pack()

# Функция для сохранения данных в JSON-файл
def save_data():
    global dataframe
    if dataframe is not None:
        updated_data = dataframe.to_dict(orient='records')
        with open(path, 'w') as file:
            json.dump(updated_data, file, indent=4)

# Создание главного окна
root = tk.Tk()
root.title("JSON Table Editor")

# Создание кнопок для загрузки и сохранения данных
load_button = tk.Button(root, text="Загрузить данные", command=load_data)
load_button.pack()

save_button = tk.Button(root, text="Сохранить данные", command=save_data)
save_button.pack()

# Создание фрейма для размещения таблицы
frame = ttk.Frame(root)
frame.pack(fill='both', expand=True)

# Запуск цикла событий tkinter
root.mainloop()





exit(0)

