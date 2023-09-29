#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import tkinter as tk
from tkinter import ttk
import pandas as pd
from pandastable import Table, TableModel


path = os.getcwd() + '\\p2p\\tixati\\l18n\\data\\data1.json'


# Функция для отображения данных в таблице
def display_data():
    # Чтение данных из JSON-файла
    try:
        data = pd.read_json(path)
    except FileNotFoundError:
        return

    # Создание нового окна для таблицы
    table_window = tk.Toplevel(root)
    table_window.title("Данные из JSON")

    # Создание и настройка виджета таблицы с использованием PandasTable
    frame = ttk.Frame(table_window)
    frame.pack(fill='both', expand=True)
    pt = Table(frame, dataframe=data, showtoolbar=True, showstatusbar=True)
    pt.show()

# Создание главного окна
root = tk.Tk()
root.title("JSON Reader")

# Создание кнопки для отображения данных
display_button = tk.Button(root, text="Показать данные", command=display_data)
display_button.pack()

# Запуск цикла событий tkinter
root.mainloop()




exit(0)

