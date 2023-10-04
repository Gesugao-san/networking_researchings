#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#import socket
from socket import gethostbyname, gaierror
from pathlib import Path

cwd = str(Path(__file__).resolve().parent)
path1 = cwd + "\\" + "hostnames2ip_in.txt"
path2 = cwd + "\\" + "hostnames2ip_out.txt"
addresses_ip, addresses_names = list(), list()
addrs1_len, addrs2_len, errors = 0, 0, 0

# https://stackoverflow.com/a/34573360
with open(path1, 'r') as file_stream:
    for address_name in file_stream:
        address_name = address_name.strip().split('://')[1].split('/')[0].split(':')[0]
        addresses_names.append(address_name)

    addrs1_len = len(addresses_names)
    # using set() to remove duplicated from list
    addresses_names = list(set(addresses_names))

    for address_name in addresses_names:
        try:
            address_ip = gethostbyname(address_name)
            addresses_ip.append(address_ip)
        except gaierror as e:
            print(f'Error getting IP address: "{address_name}"; Reason: {e}')
            errors += 1
        except Exception as e:
            print('Error getting IP address (fatal):', address_name)
            print(e)
            raise e
        #print(socket.gethostbyname(line.strip()))

addrs2_len = len(addresses_ip)
print(
    'addrs1_len:', addrs1_len,
    'addrs2_len:', addrs2_len,
    'delta:', addrs2_len-addrs1_len,
    'errors:', errors
)

with open(path2, 'w') as file:
    for address in addresses_ip:
        file.write(f'{address}\n')

exit(0)


