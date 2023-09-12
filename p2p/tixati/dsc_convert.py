#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os, csv
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
db_gen_schema = {
    'alive': None,
    'hash': None,
    'dn': None,
}
db_gen1 = {}



def line():
    print('='*10)

def dict_populate(schema, dict):
    for key in schema.keys():
        dict[key] = []

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


def loop_open_files(db_gen):
    with open(paths.txt_alive, 'r') as file:
        for line in file:
            if not line.startswith('dsc:'): continue
            line = line.rstrip()
            _line = {
                'alive': 1,
                'hash': line.split('dsc:')[1].split('?dn=')[0],
                'dn': urllib.parse.unquote(line.split('dsc:')[1].split('?dn=')[1]),
            }
            db_gen.append(_line)
    return db_gen


def write_csv(path, dictionary):
    with open(path, 'w', newline='') as csvfile1:
        writer1 = csv.DictWriter(csvfile1, fieldnames=list(db_gen_schema.keys()), delimiter=';')
        writer1.writeheader()
        for db_row in dictionary:
            writer1.writerow(db_row)
    #



if __name__ == '__main__':
    print('run')
    line()
    #dict_populate(db_gen_schema, db_gen1)
    db_gen1 = []
    db_gen1 = loop_open_files(db_gen1)
    write_csv(paths.csv_alive, db_gen1)
    line()
    print('stop')

