#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import webbrowser, os, time

cwd = os.getcwd()
filenames = [
    #'dsc_stable.txt',
    #'dsc_unstable.txt',
    #'dsc_unknown.txt',
    'dsc_unknown2.txt'
]

# https://stackoverflow.com/a/13214728/8175291
def open_tixati_channel(url):
    url = url
    print("Opening Tixati Channel URL: \"" + url + "\"")
    webbrowser.open_new(url)

def loop_open_files(filenames):
    for filename in filenames:
        with open(cwd + '\\tixati\\' + filename, 'r') as file:
            for line in file:
                if line.startswith('#'): continue
                open_tixati_channel(line.rstrip())
                time.sleep(1)



if __name__ == "__main__":
    print("run")
    #open_tixati_channel('dsc:kjawj6dwvcutvwddqw3uocudiaanrjdcofcwx3lo24fp2ns6vwua?dn=The%20Torrent%20Cache')
    print()
    loop_open_files(filenames)
    print("stop")

