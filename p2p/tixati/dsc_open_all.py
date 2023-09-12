#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import webbrowser, os, time
import urllib.parse
cwd = os.getcwd() + '\\p2p\\tixati\\data'
dsc = 'dsc:'
dn = '?dn='


paths = {
    'txt_alive': cwd + '\\txt\\dsc_manual_in_alive.txt',
    'txt_dead':  cwd + '\\txt\\dsc_manual_in_unknown.txt',
    'csv_alive': cwd + '\\csv\\dsc_alive.csv',
    'csv_dead':  cwd + '\\csv\\dsc_unknown.csv' # dsc_dead.csv'
}
sus_list = [
    'http',
    'https',
    'udp',
    'git',
    'irc',
    'magnet'
]
sus_names = []
paths_to_check = [
    #paths['csv_alive'],
    paths['csv_dead']
]



def line():
    print('='*10)

def check_dsc_name(name):
    for sus_unit in sus_list:
        if name.startswith(sus_unit):
            print('SUS NAME DETECTED!')
            sus_names.append(name)
            break
    return


#  Tixati Channel URL
# urllib.parse.urlsplit('dsc:hash1234?dn=Name'.replace(dsc, 'dsc://'))
def parse_dsc_url(url):
    # reference: 'dsc:<hash>?dn=<url_encoded_name>'
    if ((not url.startswith(dsc)) or (not dn in url)):
        print('Skipping invalid line:', url)
        return False
    url = url\
        .rstrip()\
        .split(dsc)[1]
    parsed_data = {
        'hash': url.split(dn)[0],
        'name': urllib.parse.unquote(url.split(dn)[1])
    }
    return parsed_data


def form_dsc_url(url):
    # reference: 'dsc:<hash>?dn=<url_encoded_name>'
    url['name'] = urllib.parse.quote(url['name'], encoding='UTF-8')
    data = (
        dsc +  #  NOT 'dsc://'!!!
        url['hash'] +
        dn +
        url['name']
    )
    return data


# https://stackoverflow.com/a/13214728/8175291
def open_tixati_channel(url):
    print('Go: \'' + url['name'] + '\'')
    url = form_dsc_url(url)
    webbrowser.open_new(url)
    return


def read_dsc_files(paths):
    for path in paths:
        with open(path, 'r') as file:
            for url in file:
                url = parse_dsc_url(url)
                if not url: continue
                check_dsc_name(url['name'])
                open_tixati_channel(url)
                #
                # '3.0' - very slow adding speed, for potato PC and internet connections
                # '2.0' - medium adding speed
                # '1.0' - fast adding speed
                #
                time.sleep(2.0)
    return



if __name__ == '__main__':
    print('run')
    line()
    read_dsc_files(paths_to_check)
    line()
    print('sus_names:', sus_names)
    line()
    print('stop')
    #os.exit(0)

