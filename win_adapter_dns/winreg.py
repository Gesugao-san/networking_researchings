#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import winreg

def line():
    return print('#'*10)

def get_svalue(oKey: winreg.HKEYType, name: str):
    try:
        return winreg.QueryValueEx(oKey, name)
    except FileNotFoundError:
        return None

# https://stackoverflow.com/a/5227427/8175291
def read_reg(aReg: winreg.HKEYType):
    aKey = winreg.OpenKey(
        aReg,
        #r"SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\\Interfaces",
        r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall',
        0,
        winreg.KEY_ALL_ACCESS
    )
    print(r"*** Reading from %s ***" % aKey)
    for i in range(1024):
        try:
            aValue_name = winreg.EnumKey(aKey, i)
            print(aValue_name, '	', end='')
            oKey = winreg.OpenKey(aKey, aValue_name)
            sValue = get_svalue(oKey, "DisplayName")
            print(sValue)
        except EnvironmentError as e:
            print(r"*** End reading ***")
            if not e.winerror: raise e
            if e.winerror != 259: raise e
            break
    winreg.CloseKey(aKey)
    return


if __name__ == "__main__":
    print('run', flush=True)
    line()

    aReg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
    read_reg(aReg)

    line()
    print('stop')

SystemExit(0) # exit(0)
