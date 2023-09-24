#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os

print('go')

# Открываем и читаем файл
with open(os.getcwd() + '\\p2p\\tixati\\l18n\\tixati_language_template.txt', "r") as file:
    lines = file.readlines()

category_name = "language selection window"
cat_i = 0
i = 0
for line in lines:
    i += 1
    line = line.strip()
    if line.startswith("///////"):
        print('category:', i, '+' + str(i - cat_i), line)
        cat_i = i
    elif line.startswith("//"):
        print('comment:', i, line)
        #continue
    elif line.startswith("/"):
        print('anomaly:', i, line)
