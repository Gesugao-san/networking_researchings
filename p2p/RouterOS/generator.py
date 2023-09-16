#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
cwd = os.getcwd()
code_head = """
#!/usr/bin/env bash
# -*- coding: utf-8 -*-

"""
addresses = [
    'bt.t-ru.org',
    'bt2.t-ru.org',
    'bt3.t-ru.org',
    'bt4.t-ru.org',
]

def line():
    return print('='*10)


def form_code(data_in = ""):
    data = data_in + code_head
    return data

def form_block_addresslist(data_in):
    block_head = "/ip firewall address-list" + '\n'
    data = data_in + block_head
    for address in addresses:
        data += "add address=" + address + " comment=" + address.split('.')[0] + " list=BitTorrentTrackers" + '\n'
    return data

def form_block_nat(data_in):
    block_head = "/ip firewall nat add" + "\n"
    data = data_in + block_head + """ """
    return data




"""
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
    with open(path, 'w', newline='') as rsc_file:
        writer = csv.DictWriter(csvfile, fieldnames=list(db_gen_schema.keys()), delimiter=';')
        writer.writeheader()
        for row in dictionary:
            writer.writerow(row)
    return
"""


if __name__ == '__main__':
    print('run')
    line()
    data = ""
    data = form_code(data)
    data = form_block_addresslist(data)
    print('data:', data)

    #write_csv(paths.csv_alive, db_gen1)

    line()
    print('stop')
    exit(0)

