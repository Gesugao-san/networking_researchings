#!/usr/bin/env python3
# -*- coding: iso-8859-1 -*-


import requests

proxies = {
    'http': 'http://localhost:1234',
    'https': 'http://localhost:1234',
}

response = requests.get('http://httpbin.org/get', proxies=proxies)
print(response.text)

response = requests.get('http://httpbin.org/get?arg1=hello&arg2=world', proxies=proxies)
print(response.text)


# https://stackoverflow.com/a/71341150/8175291


