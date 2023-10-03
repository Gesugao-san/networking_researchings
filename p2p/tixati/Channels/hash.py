#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import hashlib

# Функция для получения алфа-цифрового хэш-значения
def alpha_numeric_hash(input_str):
    # Создаем объект хэша SHA-256
    sha256_hash = hashlib.sha256()

    # Кодируем входную строку в байты и передаем ее хэш-функции
    sha256_hash.update(input_str.encode())

    # Получаем хэш в виде байтов
    hash_bytes = sha256_hash.digest()

    # Преобразуем байты хэша в алфа-цифровую строку (16-ричные цифры)
    alpha_numeric_hash_str = ''.join(format(b, '02x') for b in hash_bytes)

    return alpha_numeric_hash_str

try:
    # Запрос пользователю ввести строку
    user_input = input("Введите строку для хэширования: ")
    result = alpha_numeric_hash(user_input)
    print(f"Алфа-цифровое хэш-значение введенной строки: {result}")
except Exception as e:
    print(f"Произошла ошибка: {e}")

exit(0)

