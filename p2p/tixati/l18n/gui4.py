#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import tkinter as tk
from tkinter import ttk
import json
import pandas as pd


path = os.getcwd() + '\\p2p\\tixati\\l18n\\data.json'


# Функция для загрузки данных из JSON-файла и отображения их в таблице
def load_data():
    try:
        with open(path, 'r') as file:
            data = json.load(file)
            df = pd.DataFrame(data)
            display_table(df)
    except FileNotFoundError:
        display_table(pd.DataFrame(columns=['Key', 'Value']))

# Функция для отображения данных в виде таблицы
def display_table(dataframe):
    table = ttk.Treeview(frame, columns=list(dataframe.columns), show='headings')

    for col in dataframe.columns:
        table.heading(col, text=col)
        table.column(col, width=100)

    for _, row in dataframe.iterrows():
        table.insert("", "end", values=row.tolist())

    table.pack(fill='both', expand=True)

# Создание главного окна
root = tk.Tk()
root.title("JSON Table Editor")

# Создание кнопки для загрузки данных
load_button = tk.Button(root, text="Загрузить данные", command=load_data)
load_button.pack()

# Создание фрейма для размещения таблицы
frame = ttk.Frame(root)
frame.pack(fill='both', expand=True)

# Запуск цикла событий tkinter
root.mainloop()






exit(0)

