#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import webbrowser, os, csv
import urllib.parse

cwd = os.getcwd()
filenames_in = {
    'dsc_manual_in_alive.txt': 'dsc_alive.csv',
    'dsc_manual_in_unknown.txt': 'dsc_dead.csv'
}
db_gen_schema = {
    "alive": None,
    "hash": None,
    "dn": None,
}
db_gen1 = {}


def dict_populate(schema, dict):
    for key in schema.keys():
        dict[key] = []


# https://stackoverflow.com/a/13214728/8175291
def open_tixati_channel(url):
    url = url
    print("Opening Tixati Channel URL: \"" + url + "\"")
    webbrowser.open_new(url)

def loop_open_files(db_gen):
    with open(cwd + '\\tixati\\dsc_manual_in_alive.txt', 'r') as file:
        for line in file:
            if not line.startswith('dsc:'): continue
            line = line.rstrip()
            _line = {
                "alive": 1,
                "hash": line.split('dsc:')[1].split('?dn=')[0],
                "dn": urllib.parse.unquote(line.split('dsc:')[1].split('?dn=')[1]),
            }
            db_gen.append(_line)
    return db_gen

def _write1(path1, db):
    with open(path1, 'w', newline='') as csvfile1:
        writer1 = csv.DictWriter(csvfile1, fieldnames=list(db_gen_schema.keys()), delimiter=';')
        writer1.writeheader()
        for db_row in db:
            writer1.writerow(db_row)
    #



if __name__ == "__main__":
    print("run")
    #open_tixati_channel('dsc:kjawj6dwvcutvwddqw3uocudiaanrjdcofcwx3lo24fp2ns6vwua?dn=The%20Torrent%20Cache')
    print()
    #dict_populate(db_gen_schema, db_gen1)
    db_gen1 = []
    db_gen1 = loop_open_files(db_gen1)
    _write1(cwd + '\\tixati\\dsc_alive.csv', db_gen1)
    print("stop")

