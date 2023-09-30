#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import json
import pandas as pd
import sys

# Создание главного окна
root = tk.Tk()
root.title("JSON Viewer")

# Глобальная переменная для хранения DataFrame
dataframe = None
file_path = None  # Глобальная переменная для хранения текущего пути к файлу

# Функция для загрузки и отображения данных из выбранного JSON-файла
def load_data():
    global dataframe, file_path  # Сделаем dataframe и file_path глобальными переменными
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if not file_path:
        return None
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            dataframe = display_json(data, file_path)  # Обновляем dataframe
    except FileNotFoundError:
        print("Файл не найден")
    except Exception as e:
        print(f"Ошибка при загрузке данных: {str(e)}")

# Функция для отображения JSON-данных в виде таблицы
def display_json(data, file_path):
    global dataframe  # Сделаем dataframe глобальной переменной
    save_button.config(state='active') # OR entry['state'] = 'active'
    for widget in frame.winfo_children():
        widget.destroy()

    columns = ["Категория", "Ключ", "Значение"]
    records = []

    for category, category_data in data.items():
        for key, value in category_data.items():
            records.append([category, key, value])

    dataframe = pd.DataFrame(records, columns=columns)
    table = ttk.Treeview(frame, columns=columns, show="headings")

    for col in columns:
        table.heading(col, text=col)
        table.column(col, width=400, anchor="w")

    for _, row in dataframe.iterrows():
        table.insert("", "end", values=row.to_list())

    table.pack(fill="both", expand=True)

    # Функция для редактирования ячейки таблицы
    def edit_cell(event):
        item = table.selection()
        if not item:
            return
        item = item[0]
        col = table.identify_column(event.x)
        col_id = col[1]
        current_value = table.item(item, 'values')[int(col_id)-1]

        # Создаем диалоговое окно для редактирования значения
        edit_window = tk.Toplevel(root)
        edit_window.title("Редактирование Ячейки")
        edit_window.minsize(len(current_value)+1, edit_window.winfo_height())

        label = tk.Label(edit_window, text="Старое значение:")
        label.pack()

        old_value = tk.Entry(edit_window, width=len(current_value))
        old_value.insert(0, current_value)
        old_value.config(state='disabled') # OR entry['state'] = 'disabled'
        old_value.pack()

        label = tk.Label(edit_window, text="Новое значение:")
        label.pack()

        edit_entry = tk.Entry(edit_window, width=len(current_value))
        edit_entry.insert(0, current_value)
        edit_entry.pack()

        def save_edit():
            new_value = edit_entry.get()
            table.item(item, values=(*table.item(item)['values'][:int(col_id)-1], new_value, *table.item(item)['values'][int(col_id)-1 + 1:]))
            # Обновляем данные в DataFrame
            category = table.item(item, 'values')[0]
            key = table.item(item, 'values')[1]
            dataframe.loc[(dataframe['Категория'] == category) & (dataframe['Ключ'] == key), col_id] = new_value
            edit_window.destroy()

        save_button = tk.Button(edit_window, text="Сохранить", command=save_edit)
        save_button.pack()

    table.bind('<Double-1>', edit_cell)

    return dataframe  # Возвращаем dataframe

# Функция для сохранения JSON-файла с данными
def save_data():
    global dataframe, file_path  # Сделаем dataframe и file_path глобальными переменными
    if dataframe is None:
        print("Данные не загружены.")
        return
    if file_path is None:
        print("Выберите JSON-файл для сохранения.")
        return
    try:
        data_to_save = {}
        for _, row in dataframe.iterrows():
            category = row["Категория"]
            key = row["Ключ"]
            value = row["Значение"]
            if category not in data_to_save:
                data_to_save[category] = {}
            data_to_save[category][key] = value

        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data_to_save, file, ensure_ascii=False, indent=4)

        print(f"Данные сохранены в файл: {file_path}")
    except Exception as e:
        print(f"Ошибка при сохранении данных: {str(e)}")

# Кнопка для выбора JSON-файла
load_button = tk.Button(root, text="Выбрать JSON-файл", command=load_data)
load_button.pack(pady=10)

# Кнопка для сохранения JSON-файла
save_button = tk.Button(root, text="Сохранить JSON-файл", command=save_data)
save_button.config(state='disabled') # OR entry['state'] = 'disabled'
save_button.pack(pady=10)

# Фрейм для размещения таблицы
frame = ttk.Frame(root, width=250, height=200)
frame.pack(fill="both", expand=True)

# Завершение программы при закрытии окна
root.protocol("WM_DELETE_WINDOW", lambda: sys.exit(0))

# Запуск цикла событий tkinter
root.mainloop()
