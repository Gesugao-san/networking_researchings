#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#import socket
import errno
import os
from socket import getaddrinfo, AF_INET, IPPROTO_TCP, gaierror, socket
from pathlib import Path
import requests
from urllib.parse import urlparse
from urllib3.exceptions import NameResolutionError
from urllib3.exceptions import HTTPError
from requests.adapters import HTTPAdapter, Retry

cwd = str(Path(__file__).resolve().parent) + "\\"
path1 = cwd + "hostnames2ip_in.txt"
path2 = cwd + "hostnames2ip_out.txt"
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
    return print('-'*10)


def return_port(netloc):
    port = 80
    if ":" in netloc:
        netloc, port = netloc.split(':')
    return netloc, port


# https://stackoverflow.com/a/34573360
def open_f(path):
    global addrs1_len, addresses_names
    with open(path, 'r') as file_stream:
        for host in file_stream:
            data = urlparse(host)._asdict()
            data['url'] = host.strip()
            #data['scheme'], data['host'] = host.strip().split('://')
            #data['host'], data['path'] = data['host'].split('/')

            data['netloc'], data['port'] = return_port(data['netloc'])

            #if len(host) != 2:
            #    host = [host, 80]
            #host, port = host[0], host[1]

            print(data)
            addresses_names.append(data)
            break

        addrs1_len = len(addresses_names)
        # using set() to remove duplicated from list
        #addresses_names = list(set(addresses_names))


def check_status(data):
    for data in addresses_names:
        HOST = str(data['netloc'])
        PORT = str(data['port'])
        URL  = str(data.get('url'))

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
            s.mount(f"{data['netloc']}+://", adapter)
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

    open_f(path1)

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



