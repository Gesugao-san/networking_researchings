#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#import socket
import csv
import errno
import os
import requests

from pathlib import Path
from requests.adapters import HTTPAdapter, Retry
from socket import getaddrinfo, AF_INET, IPPROTO_TCP, gaierror, socket
from urllib.parse import urlparse
from urllib3.exceptions import HTTPError
from urllib3.exceptions import NameResolutionError

# see https://github.com/python/typeshed/blob/main/stdlib/_typeshed/README.md
from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    from _typeshed import FileDescriptorOrPath
else:
    StrPath: TypeAlias = str | os.PathLike[str]
    BytesPath: TypeAlias = bytes | os.PathLike[bytes]
    FileDescriptorOrPath: TypeAlias = int | StrPath | BytesPath


cwd = str(Path(__file__).resolve().parent) + "\\"
path1 = cwd + "hostnames2ip_in.txt"
path2 = cwd + "hostnames2ip_out.txt"

files = {
    'user_input': cwd + "tracker_score_in.txt",
    'csv_db': cwd + "tracker_score.csv"
}

db_template = [
    {
        'category': 'General',
        'key': 'url',
        'hint': 'URL of this host.',
        'type': str,
        'default': None
    },
    {
        'category': 'Checks',
        'key': 'checks',
        'hint': 'Total number of checks of this host.',
        'type': int,
        'default': 0
    },
    {
        'category': 'Checks',
        'key': 'ok',
        'hint': 'Number of successful connections.',
        'type': int,
        'default': 0
    },
    {
        'category': 'Checks',
        'key': 'warn',
        'hint': 'Number of overloads and etc.',
        'type': int,
        'default': 0
    },
    {
        'category': 'Checks',
        'key': 'bad',
        'hint': 'Number of fatal errors or DNS failure.',
        'type': int,
        'default': 0
    },
    {
        'category': 'Protocols',
        'key': 'http',
        'hint': 'Indicates host supported protocol.',
        'type': int, # bool(int)
        'default': 2 # "not checked yet"
    },
    {
        'category': 'Protocols',
        'key': 'https',
        'hint': 'Indicates host supported protocol.',
        'type': int, # bool(int)
        'default': 2 # "not checked yet"
    },
    {
        'category': 'Protocols',
        'key': 'udp',
        'hint': 'Indicates host supported protocol. Preferred in most cases.',
        'type': int, # bool(int)
        'default': 2 # "not checked yet"
    },
    {
        'category': 'Protocols',
        'key': 'ws',
        'hint': 'Indicates host supported protocol.',
        'type': int, # bool(int)
        'default': 2 # "not checked yet"
    },
    {
        'category': 'Protocols',
        'key': 'wss',
        'hint': 'Indicates host supported protocol.',
        'type': int, # bool(int)
        'default': 2 # "not checked yet"
    },
    {
        'category': 'Fingerprint',
        'key': 'last_ipv4',
        'hint': 'Last known IPv4 of this host. Helps when DNS is inaccessible.',
        'type': str,
        'default': None
    },
    {
        'category': 'Timeline',
        'key': 'last_check',
        'hint': 'Timestamp of last check attempt.',
        'type': int,
        'default': None
    },
    {
        'category': 'Timeline',
        'key': 'last_ok',
        'hint': 'Timestamp of last successful connection.',
        'type': int,
        'default': None
    },
    {
        'category': 'Timeline',
        'key': 'last_warn',
        'hint': 'Timestamp of last connection with warning.',
        'type': int,
        'default': None
    },
    {
        'category': 'Timeline',
        'key': 'last_err',
        'hint': 'Timestamp of last connection with host/DNS error.',
        'type': int,
        'default': None
    },
    {
        'category': 'Details',
        'key': 'last_err_details',
        'hint': 'Details about last fatal connection.',
        'type': str,
        'default': None
    }
]

fieldnames = []
for i in db_template:
    fieldnames.append(i['key'])

my_dialect = csv.excel
my_dialect.delimiter=';'

addresses_ip, addresses_names = list(), list()
addrs1_len, addrs2_len, errors = 0, 0, 0


# https://habr.com/ru/companies/ruvds/articles/472858/
# https://stackoverflow.com/a/35504626/8175291
s = requests.Session()
retries = Retry(
    total = 5,
    backoff_factor = 0.1,
    status_forcelist = [500, 502, 503, 504]
)
adapter = requests.adapters.HTTPAdapter(
    pool_connections = 10,
    pool_maxsize = 10,
    max_retries = retries
)


def line():
    return print('#'*10)


def get_port(netloc: str):
    """Returns the port, because urllib urlparse doesn't parse it properly.

    Args:
        netloc (str): urlparse netloc.

    Returns:
        str: netloc (without port).
        int: port.
    """
    port = 80
    if ":" in netloc:
        netloc, port = netloc.split(':')
    return netloc, port


def db_get_default_line(template: dict):
    line = {}
    for db_entry in template:
        line[db_entry['key']] = db_entry['default']
    return line


def db_sort_lines(lines: list):
    lines.sort()
    return lines


def db_read_input(file: FileDescriptorOrPath):
    line = db_get_default_line(db_template)
    lines_raw = []
    lines = []

    with open(file, 'r') as handler:
        for line_raw in handler:
            lines_raw.append(line_raw)
            break

    lines_raw = db_sort_lines(lines_raw)
    #print('lines_raw', lines_raw)

    for line_raw in lines_raw:
        line['url'] = line_raw.strip()
        lines.append(line)
    #print('lines', lines)
    return lines


def db_write(file: FileDescriptorOrPath, db: dict):
    with open(file, 'w', newline='') as handler:
        csvW = csv.DictWriter(handler, fieldnames=fieldnames, dialect=my_dialect)
        csvW.writeheader()
        for db_row in db:
            csvW.writerow(db_row)


def db_read(file: FileDescriptorOrPath):
    with open(file, 'r') as handler:
        reader = csv.reader(handler, dialect=my_dialect)
        for row in reader:
            print(row)




# https://stackoverflow.com/a/34573360
def read_f(file: FileDescriptorOrPath):
    global addrs1_len, addresses_names
    with open(file, 'r') as handler:
        for host in handler:
            urldict = urlparse(host)._asdict()
            urldict['url'] = host.strip()
            #urldict['scheme'], urldict['host'] = host.strip().split('://')
            #urldict['host'], urldict['path'] = urldict['host'].split('/')

            urldict['netloc'], urldict['port'] = get_port(urldict['netloc'])

            #if len(host) != 2:
            #    host = [host, 80]
            #host, port = host[0], host[1]

            print(urldict)
            addresses_names.append(urldict)
            break

        addrs1_len = len(addresses_names)
        # using set() to remove duplicated from list
        #addresses_names = list(set(addresses_names))


def check_status(urldict: dict):
    for urldict in addresses_names:
        HOST = str(urldict['netloc'])
        PORT = str(urldict['port'])
        URL  = str(urldict.get('url'))

        """
        # https://stackoverflow.com/q/13325956/8175291
        try:
            addrInfo = getaddrinfo(HOST, PORT, AF_INET, IPPROTO_TCP)
            print(addrInfo)
        except gaierror as e:
            if not e.errno:
                print(f'Error getting IP address: "{HOST}:{PORT}", code: {e.errno}, reason: {e}')
                errors += 1
                continue
            print(e)
            #ee = socket.errorTab[e.errno]
            #print(ee)
            #print(errno.errorcode(ee))
            if e.errno != 10044:
                print(f'Error getting IP address: "{HOST}:{PORT}", code: {e.errno}, reason: {e}')
                errors += 1
                continue
            print(f"{HOST}:{PORT}: [GAIError] Hostname can't be resolved — No known DNS Records. Recovery is unlikely.")
        except Exception as e:
            print(f'{HOST}:{PORT}: [GAIError (fatal)] {e}')
            raise e
        #print(socket.gethostbyname(line.strip()))
        print('-'*10)
        """

        # https://stackoverflow.com/a/71453648/8175291
        # https://stackoverflow.com/a/16511493/8175291
        try:
            s.mount(f"{urldict['netloc']}+://", adapter)
            r = s.get(URL)#, timeout=(5, 8.5))
            r.raise_for_status()
            print(r.json())
        except requests.exceptions.HTTPError as e:
            print(f"{URL}: [{str(e.__class__.__name__)}] {str(e.__doc__)}")
            print(e)
            continue
        except requests.exceptions.ConnectionError as e:
            print(f"{URL}: [{str(e.__class__.__name__)}] {str(e.__doc__)}")
            print(e)
            continue
        except requests.exceptions.Timeout as e:
            # Maybe set up for a retry, or continue in a retry loop
            print(f"{URL}: [{str(e.__class__.__name__)}] {str(e.__doc__)}")
            print(e)
            continue
        except requests.exceptions.TooManyRedirects as e:
            # Tell the user their URL was bad and try a different one
            print(f"{URL}: [{str(e.__class__.__name__)}] {str(e.__doc__)}")
            print(e)
            continue
        except requests.exceptions.RequestException as e:
            # https://stackoverflow.com/a/4308202/8175291
            print(f"{URL}: [{str(e.__class__.__name__)}] {str(e.__doc__)}")
            print(e)
            continue #raise SystemExit(e)

        exit(0)


if __name__ == "__main__":
    print('run', flush=True)
    line()

    print('fieldnames:', fieldnames)
    read_f(path1)

    db = {}
    db = db_read_input(files['user_input'])
    #print(db)
    db_write(files['csv_db'], db)
    db_read(files['csv_db'])


    addrs2_len = len(addresses_ip)
    print(
        'addrs1_len:', addrs1_len,
        'addrs2_len:', addrs2_len,
        'delta:', addrs2_len-addrs1_len,
        'errors:', errors
    )

    #with open(path2, 'w') as file:
    #    for address in addresses_ip:
    #        file.write(f'{address}\n')

    line()
    print('stop')

SystemExit(0) # exit(0)



