#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import webbrowser

filenames = ['./dsc_stable.txt', './dsc_unstable.txt', './dsc_unknown.txt']
# https://stackoverflow.com/a/13214728/8175291
#webbrowser.open_new('steam://defrag/440')
webbrowser.open_new('dsc:kjawj6dwvcutvwddqw3uocudiaanrjdcofcwx3lo24fp2ns6vwua?dn=The%20Torrent%20Cache')

def open_tixati_channel(url):
    webbrowser.open_new('dsc:kjawj6dwvcutvwddqw3uocudiaanrjdcofcwx3lo24fp2ns6vwua?dn=The%20Torrent%20Cache')

for filename in filenames:
    with open(filename) as file:
        for line in file:
            print(line.rstrip())



if __name__ == "__main__":
    print("run")
    print()
    dict_populate(db_in_schema, db_in)
    print()
    print("stop")

