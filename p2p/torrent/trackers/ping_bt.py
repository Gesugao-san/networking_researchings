#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import httpie
#$ http GET "https://torrent.ubuntu.com/announce?info_hash=%90%28%9F%D3M%FC%1C%F8%F3%16%A2h%AD%D85L%853DX&amp;peer_id=-PC0001-706887310628&amp;uploaded=0&amp;downloaded=0&amp;left=699400192&amp;port=6889&amp;compact=1"
#unescape(unquote('https://v.w.xy/'))


import requests
import random
import urllib
#import urllib.parse
from urllib.request import quote, unquote
from html import escape, unescape
from urllib3.exceptions import NewConnectionError
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


# "ubuntu-14.10-desktop-amd64.iso"
# -<2-символьный id><номер версии из 4 цифр>-
peer_id = '-PC0001-' + ''.join([str(random.randint(0, 9)) for _ in range(12)])
payload = {
    'info_hash': 'b415c913643e5ff49fe37d304bbb5e6e11ad5101',
    'peer_id': peer_id, #'BAPsa41-dsg0rbz223v1',
    'uploaded': 0,
    'downloaded': 0,
    'left': 699400192,
    'port': 6889,
    'compact': 1,
}
payload_port = {
    'port': 6889
}
#headers = {'user-agent': 'my-app/0.0.1'}
print('peer_id:', peer_id)


def line(text=''):
    one_line = '='*10
    if (text != ''):
        return print(one_line, text, one_line)
    return print(one_line * 3)

def ping_bt(url, payload):
    #urllib.parse.unquote(url)
    session = requests.Session()
    retry = Retry(
        connect=1,
        backoff_factor=1.5
    )
    adapter = HTTPAdapter(max_retries=1)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    session.mount('udp://', adapter)
    try:
        line('CONNECTING')
        print('Trying to connecting to: "' + url + '"... ', end='')
        r = session.get(url)#, params=payload) #, auth=('user', 'pass'))
    except ConnectionRefusedError as E: # Built-in Exception
        return print('fail!\nConnectionRefusedError:', E)
    except requests.exceptions.ConnectionError as E:
        return print('fail!\nConnection refused:', E)
    print('connected!\nstatus_code:', r.status_code)
    print_bt(r)
    return

def print_bt(r):
    line('DETAILS')
    print('url:', r.url)
    print('status_code:', r.status_code)
    print('headers:', r.headers)
    print('encoding:', r.encoding)
    print('text:', r.text)
    print('r:', r)
    line()



if __name__ == "__main__":
    print("run")
    line()
    print()

    #ping_bt('http://torrent.ubuntu.com:80/announce', payload) {ISO-8859-1; d14:failure reason63:Requested download is not authorized for use with this tracker.e}
    payload['port'] = 6969
    #ping_bt('http://tracker.dler.org/announce', payload) # Max retries exceeded with url: /announce
    #ping_bt('http://tracker.files.fm/announce', payload) # Max retries exceeded with url: /announce
    #ping_bt('https://bt1.lan:6969/announce', payload) # File "C:\Python311\Lib\ssl.py", line 1346, in do_handshake
    ping_bt('http://bt1.lan:6969/announce', payload)
    #ping_bt('udp://bt1.lan:6969/announce', payload) # requests.exceptions.InvalidURL: Not supported URL scheme udp
    #ping_bt('bt1.lan:6969/announce', payload) # requests.exceptions.InvalidSchema: No connection adapters were found for
    payload['port'] = 443
    ping_bt('https://tracker.lilithraws.org:443/announce', payload) # 403
    ping_bt('https://tracker.loligirl.cn:443/announce', payload) # d14:failure reason31:no info_hash parameter suppliede

    print()
    line()
    print("stop")
    exit(0)


