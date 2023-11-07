#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json
#import wmi
from wmi import WMI
from datetime import datetime as dt
#import wmi_client_wrapper as wmi


param_list = [
    ['DefaultIPGateway', 'DefaultIPGateway', 0],
    ['DHCPServer', 'DHCPServer', None],
    ['DNSHostName', 'DNSHostName', None],
    ['IPv4Address', 'IPAddress', 0],
    ['IPv6Address', 'IPAddress', 1],
    ['IPSubnet', 'IPSubnet', 0],
    ['MACAddress', 'MACAddress', None],
    ['ServiceName', 'ServiceName', None]
]

def line():
    return print('#'*10)

# https://stackoverflow.com/a/75666480/8175291
def wmiToDict(wmi_object):
    return dict((attr, getattr(wmi_object, attr)) for attr in wmi_object.__dict__['_properties'])

# Network Interface
# https://codeby.net/threads/81633/
# https://stackoverflow.com/a/11785020/8175291
def nic_wmi() -> (dict, bool):
    nic = dict()
    conn = WMI()
    descriptions = [it.Description for it in conn.Win32_NetworkAdapter() if it.PhysicalAdapter]
    if not descriptions:
        return False
    for it in conn.Win32_NetworkAdapterConfiguration():
        if not it.Description in descriptions:  # if not listed in GUI
            continue
        desc = it.Description
        itd = wmiToDict(it)
        nic[desc] = dict()
        #props = list(it.properties.keys())
        #props['Description'] = desc
        #print('it.props:', json.dumps(props, indent=2))
        for param in param_list:
            param_data = {param[0]: itd.get(param[1], None)}
            if isinstance(param[2], int) and param_data[param[0]]:
                param_data[param[0]] = param_data[param[0]][param[2]]
            nic[desc].update(param_data)
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

    data = nic_wmi()
    print(json.dumps(data, indent=2))
    #wmi_ni()

    line()
    print('stop')

SystemExit(0) # exit(0)
