#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import asyncio
#from os import getrandom
from aiobtdht import DHT
from aioudp import UDPServer


async def main(loop):
    initial_nodes = [
        ("67.215.246.10", 6881),  # router.bittorrent.com
        ("87.98.162.88", 6881),  # dht.transmissionbt.com
        ("82.221.103.244", 6881)  # router.utorrent.com
    ]

    udp = UDPServer()
    udp.run("0.0.0.0", 12346, loop=loop)

    dht = DHT(int("0x54A10C9B159FC0FBBF6A39029BCEF406904019E0", 16), server=udp, loop=loop)

    print("bootstrap")
    await dht.bootstrap(initial_nodes)
    print("bootstrap done")

    print("search peers for Linux Mint torrent (8df9e68813c4232db0506c897ae4c210daa98250)")
    peers = await dht[bytes.fromhex("8df9e68813c4232db0506c897ae4c210daa98250")]
    print("peers:", peers)

    print("peer search for ECB3E22E1DC0AA078B48B7323AEBBA827AD9BD80")
    peers = await dht[bytes.fromhex("ECB3E22E1DC0AA078B48B7323AEBBA827AD9BD80")]
    print("peers:", peers)

    print("announce with port `2357`")
    await dht.announce(bytes.fromhex("ECB3E22E1DC0AA078B48B7323AEBBA827AD9BD80"), 2357)
    print("announce done")

    print("search our own ip")
    peers = await dht[bytes.fromhex("ECB3E22E1DC0AA078B48B7323AEBBA827AD9BD80")]
    print("peers:", peers)


if __name__ == '__main__':
    print("Initializing DHT", flush=True)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.run_forever()
    exit(0)


