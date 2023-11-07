#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import win32api
import win32con


def line():
    return print('#'*10)

# https://stackoverflow.com/a/75914805/8175291
def read_reg():
    # Open the network adapter key in the registry
    handle = win32api.RegOpenKeyEx(
        win32con.HKEY_LOCAL_MACHINE,
        r'SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces',
        0,
        win32con.KEY_ALL_ACCESS
    )
    win32api.RegCloseKey(handle)
    print('handle', handle)


if __name__ == "__main__":
    print('run', flush=True)
    line()

    read_reg()

    line()
    print('stop')

SystemExit(0) # exit(0)
