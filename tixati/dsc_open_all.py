#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import webbrowser, os, time
import urllib.parse

cwd = os.getcwd()
filenames = [
    #'dsc_alive.csv',
    'dsc_unknown.csv'
]
sus_list = [
    'http',
    'https',
    'udp',
    'git',
    'irc',
    'magnet'
]
sus_names = []


def check_dcs_name(name):
    for sus_unit in sus_list:
        if name.startswith(sus_unit):
            print('SUS:', name)
            sus_names.append(name)
            break
    return


# Tixati Channel URL
def parse_dcs_url(url):
    # reference: "dsc:<hash>?dn=<url_encoded_name>"
    if not url.startswith('dsc:') or not '?dn=' in url:
        print('Invalid URL:', url)
        return False
    url = url\
        .rstrip()\
        .split('dsc:')[1]
    parsed_data = {
        "hash": url.split('?dn=')[0],
        "name": urllib.parse.unquote(url.split('?dn=')[1])
    }
    return parsed_data


def form_dcs_url(url):
    # reference: "dsc:<hash>?dn=<url_encoded_name>"
    data = "dcs:" + url["hash"] + "?dn=" + url["name"]
    return data


# https://stackoverflow.com/a/13214728/8175291
def open_tixati_channel(url):
    url = url
    print("Go: \"" + url["name"] + "\"")
    webbrowser.open_new(form_dcs_url(url))
    return

def loop_open_files(filenames):
    for filename in filenames:
        with open(cwd + '\\tixati\\' + filename, 'r') as file:
            for url in file:
                url = parse_dcs_url(url)
                if not url: continue
                check_dcs_name(url['name'])
                open_tixati_channel(url)
                #
                # "3.0" - too slow adding speed, for potato PC
                # "2.0" - medium adding speed
                # "1.0" - fast adding speed
                #
                time.sleep(2.0)
    return



if __name__ == "__main__":
    print("run")
    #open_tixati_channel('dsc:kjawj6dwvcutvwddqw3uocudiaanrjdcofcwx3lo24fp2ns6vwua?dn=The%20Torrent%20Cache')
    print()
    loop_open_files(filenames)
    print()
    print('sus_names:', sus_names)
    print("stop")
    os.exit(0)

