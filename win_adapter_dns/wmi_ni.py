#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json
#import wmi
from wmi import WMI
from datetime import datetime as dt
#import wmi_client_wrapper as wmi


def line():
    return print('#'*10)

def get_wmi_value(key, value):
    # try:
    #     return value
    # except AttributeError: #TypeError:
    #     return None
    #
    #if value in key.properties:
    #    return key.value
    return key.value if value in key.properties else None

# Network Interface
# https://codeby.net/threads/81633/
# https://stackoverflow.com/a/11785020/8175291
def nic_wmi() -> (dict, bool):
    nic = dict()
    conn = WMI()
    description = [it.Description for it in conn.Win32_NetworkAdapter() if it.PhysicalAdapter]
    if description:
        for it in conn.Win32_NetworkAdapterConfiguration():
            if it.Description in description:
                desc = it.Description
                nic[desc] = dict()
                #param_list = []
                #nic[desc].update({"DefaultIPGateway": get_wmi_value(it, 'DefaultIPGateway[0]')})
                try:
                    nic[desc].update({"DefaultIPGateway": it.DefaultIPGateway[0]})
                except TypeError:
                    nic[desc].update({"DefaultIPGateway": None})
                try:
                    nic[desc].update({"DHCPServer": it.DHCPServer})
                except TypeError:
                    nic[desc].update({"DHCPServer": None})
                try:
                    nic[desc].update({"DNSHostName": it.DNSHostName})
                except TypeError:
                    nic[desc].update({"DNSHostName": None})
                try:
                    nic[desc].update({"IPv4Address": it.IPAddress[0]})
                except TypeError:
                    nic[desc].update({"IPv4Address": None})
                try:
                    nic[desc].update({"IPv6Address": it.IPAddress[1]})
                except TypeError:
                    nic[desc].update({"IPv6Address": None})
                try:
                    nic[desc].update({"IPSubnet": it.IPSubnet[0]})
                except TypeError:
                    nic[desc].update({"IPSubnet": None})
                try:
                    nic[desc].update({"MACAddress": it.MACAddress})
                except TypeError:
                    nic[desc].update({"MACAddress": None})
                try:
                    nic[desc].update({"ServiceName": it.ServiceName})
                except TypeError:
                    nic[desc].update({"ServiceName": None})
    return nic if nic else False

def wmi_ni():
    c = WMI()
    ni = c.Windows.Networking.Connectivity.NetworkInformation
    profile = ni.GetInternetConnectionProfile()
    if profile:
        interface = profile.NetworkAdapter.IanaInterfaceType
        if interface == 71:
            print('do WiFi stuff')
        elif interface == 6:
            print('do Ethernet stuff')
        else:
            print('do wtf stuff')



if __name__ == "__main__":
    print('run', flush=True)
    line()

    print(json.dumps(nic_wmi(), indent=2))
    #wmi_ni()

    line()
    print('stop')

SystemExit(0) # exit(0)
