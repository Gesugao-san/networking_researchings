#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import hashlib

def alpha_numeric_hash(input_str):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_str.encode())
    hash_bytes = sha256_hash.digest()

    # Преобразование байтов хэша в строку
    alpha_numeric_characters = "abcdefghijklmnopqrstuvwxyz0123456789"
    alpha_numeric_hash_str = ''.join(alpha_numeric_characters[b % len(alpha_numeric_characters)] for b in hash_bytes)

    return alpha_numeric_hash_str

try:
    user_input = input("Введите строку для хэширования: ")
    result = alpha_numeric_hash(user_input)
    print(f"Алфа-цифровое хэш-значение введенной строки: {result}")
except Exception as e:
    print(f"Произошла ошибка: {e}")


exit(0)

