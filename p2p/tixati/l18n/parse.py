#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import json

data = {
    "categories": {},
    "comments": [],
    "anomalies": []
}

print('go')


with open(os.getcwd() + '\\p2p\\tixati\\l18n\\tixati_language_template.txt', "r") as file:
    lines = file.readlines()
#for _ in range(4):
#    lines.append('\n')

cat_name = None  # "language selection window"
cat_i = 0
data['categories'][cat_name] = {}

i = 0
i_max = len(lines)
for line in lines:
    i += 1
    delimiter = line.strip()
    if (i > (len(lines) - 3)):
        print(i_max, i)
        break
    key = lines[i + 1].strip()
    value = lines[i + 2].strip()

    #if i == 1:
    #    continue

    if delimiter != "" and key == "":
        continue

    if key.startswith("/////// "):
        category = key.split("/////// ")[1]
        print('category:', i, '+' + str(i - cat_i), category)
        cat_i = i
        cat_name = category
        data['categories'][cat_name] = {}
        continue
    if key.startswith("// "):
        comment = key.split("// ")[1]
        print('comment:', i, comment)
        #data['comments'].append(key)
        continue
    if key.startswith("/"):
        print('anomaly:', i, key)
        data['anomalies'].append(key)
        continue

    if (delimiter == '') and (key != ''):
        #print('key: "'+str(key)+'"; value:"'+str(value)+'"')
        data['categories'][cat_name][key] = value
        print([cat_name, key, value])


#print('data', data)
print('=' * 50)
#print('categories', json.dumps(list(data['categories'].keys()), indent=2))


exit(0)

