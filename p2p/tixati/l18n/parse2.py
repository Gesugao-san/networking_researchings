#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json
import tkinter as tk
from tkinter import filedialog
from tkinter import Scrollbar

# Создаем главное окно
root = tk.Tk()
root.title("Отображение значений из файла")

# Создаем текстовое поле для вывода значений
text_widget = tk.Text(root, height=40, width=160)
text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Добавляем полосу прокрутки
scrollbar = Scrollbar(root, command=text_widget.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_widget.config(yscrollcommand=scrollbar.set)

# Устанавливаем значение по умолчанию
cat_num = 0
parsed_data = {}  # Словарь для хранения данных после разбора файла
parsed_data[f'{cat_num:03d}. comments'] = {}
cat_num += 1
category = f'{cat_num:03d}. language_window'
parsed_data[category] = {}

def widget_clear():
    text_widget.delete(1.0, tk.END)  # Очищаем текстовое поле

def widget_print(data, index = tk.END):
    text_widget.insert(index, data)  # Выводим Категорию, Ключ, Значение

# Функция для открытия файла через диалоговое окно
def open_file_dialog():
    global category, parsed_data  # Сделаем category и parsed_data глобальными переменными
    file_types = [
        ("Text Files (Tixati Language)", "*.txt"),
        ("Json File", "*.json"),
        ("All Files", "*.*")
    ]
    path = filedialog.askopenfilename(filetypes=file_types)
    if not path:
        return
    filename = path.split('/')[len(path.split('/'))-1]
    print(f"File \"{filename}\" was opened, see app window to more.")
    widget_clear()
    widget_print(f"File \"{filename}\" content:\n")
    if path.endswith(".json"):
        with open(path, 'r') as file:
            parsed_data = json.load(file)
        widget_print(json.dumps(parsed_data, indent=2)) # Выводим Категорию, Ключ, Значение
    else:
        with open(path, "r") as file:
            lines = file.readlines()
        parse_txt_file(lines)  # Вызываем функцию для разбора файла

# Функция для разбора файла и вывода данных
def parse_txt_file(lines):
    # Сделаем category и parsed_data глобальными переменными
    global category, parsed_data, cat_num
    #line_num = -1
    for line_num, line in enumerate(lines, start = -1):
        line_num += 1
        line = line.strip()
        if line.startswith("///////"):
            cat_num += 1
            widget_print(f"{json.dumps({category: parsed_data[category]}, indent=2)},\n")
            category = f'{cat_num:03d}. ' + line[len("/////// "):]  # Удаляем "/////// " из начала строки
            if not category in parsed_data:
                parsed_data[category] = {}
            continue
        # Пропускаем разделители — пустые строки
        if not line:
            continue
        # Игнорируем комментарии
        if line.startswith("//"):
            comment = line[len("// "):]
            # Если следующая строка является разделителем -
            # вставляем новую строку в комментарий
            for i in range(1, 4):
                if not lines[line_num + i].replace('\r', '').startswith('\n'):
                    break
                comment += '\n'
            parsed_data[f'{0:03d}. comments'][f'{line_num:05d}'] = comment
            continue
        key = line
        value = lines.pop(line_num + 1).strip()  # Получаем следующую строку (Значение)
        parsed_data[category][key] = value  # Добавляем данные в список
    print(f"Items was parsed: Categories: {cat_num}; Lines: {line_num}.")

# Кнопка для выбора файла через диалоговое окно
open_button = tk.Button(root, text="Выбрать файл", command=open_file_dialog)
open_button.pack()

# Функция для сохранения данных в JSON файл
def save_json(data):
    file_types = [("JSON Files", "*.json"), ("All Files", "*.*")]
    path = filedialog.asksaveasfilename(filetypes=file_types, defaultextension=".json")
    if path:
        with open(path, "w") as json_file:
            json.dump(data, json_file, indent=2)
        print(f"Данные сохранены в файл: \"{path}\".")

# Кнопка для сохранения JSON файла
save_button = tk.Button(root, text="Сохранить JSON", command=lambda: save_json(parsed_data))
save_button.pack()

print("Welcome.")

# Завершение программы при закрытии окна
root.protocol("WM_DELETE_WINDOW", lambda: sys.exit(0))

# Запускаем главный цикл приложения
root.mainloop()

print("Goodbye.")
