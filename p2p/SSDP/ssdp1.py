#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import asyncio
import socket

from ssdp import aio, messages, network


class MyProtocol(aio.SimpleServiceDiscoveryProtocol):

    def response_received(self, response, addr):
        print(response, addr)

    def request_received(self, request, addr):
        print(request, addr)


loop = asyncio.get_event_loop()
connect = loop.create_datagram_endpoint(MyProtocol, family=socket.AF_INET)
transport, protocol = loop.run_until_complete(connect)

notify = messages.SSDPRequest('NOTIFY')
notify.sendto(transport, (network.MULTICAST_ADDRESS_IPV4, network.PORT))

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

transport.close()
loop.close()






