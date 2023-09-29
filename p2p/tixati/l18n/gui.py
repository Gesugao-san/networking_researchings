#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import tkinter as tk


path = os.getcwd() + '\\p2p\\tixati\\l18n\\data\\data1.json'


# Создать функцию для отображения данных в формате "Ключ: Значение"
def display_data():
    # Получить данные из текстовых полей
    key = key_entry.get()
    value = value_entry.get()

    # Форматировать данные
    formatted_data = f"Ключ: {key}, Значение: {value}"

    # Очистить текстовое поле для вывода
    output_text.delete(1.0, tk.END)

    # Вывести отформатированные данные
    output_text.insert(tk.END, formatted_data)

# Создать главное окно
root = tk.Tk()
root.title("Пример программы с tkinter")

# Создать и разместить элементы управления на главном окне
key_label = tk.Label(root, text="Ключ:")
key_label.pack()

key_entry = tk.Entry(root)
key_entry.pack()

value_label = tk.Label(root, text="Значение:")
value_label.pack()

value_entry = tk.Entry(root)
value_entry.pack()

display_button = tk.Button(root, text="Показать данные", command=display_data)
display_button.pack()

output_text = tk.Text(root, height=5, width=30)
output_text.pack()

# Запустить цикл событий tkinter
root.mainloop()



exit(0)

