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
    return print('='*10)

def dict_populate(schema, dict):
    for key in schema.keys():
        dict[key] = []
    return

def check_dsc_name(name):
    for sus_unit in sus_list:
        if name.startswith(sus_unit):
            print('SUS NAME DETECTED!')
            sus_names.append(name)
            break
    return


#  Tixati Channel URL
# urllib.parse.urlsplit('dsc:hash1234?dn=Name'.replace(dsc, 'dsc://'))
def parse_dsc(url):
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


def read_txt(path):
    data = []
    with open(path, 'r') as file:
        for url in file:
            url = parse_dsc(url)
            if not url: continue
            data.append(url)
    return data


def read_csv(path):
    data = []
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            data.append(row)
    return data


def write_csv(path, dictionary):
    with open(path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=list(db_gen_schema.keys()), delimiter=';')
        writer.writeheader()
        for row in dictionary:
            writer.writerow(row)
    return



if __name__ == '__main__':
    print('run')
    line()
    #dict_populate(db_gen_schema, db_gen1)

    csv_alive = read_csv(paths['csv_alive'])
    csv_dead  = read_csv(paths['csv_dead'])

    txt_alive = read_txt(paths['txt_alive'])
    txt_dead  = read_txt(paths['txt_dead'])

    write_csv(paths.csv_alive, db_gen1)

    line()
    print('stop')
    os.exit(0)

