#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import btdht
import binascii

def find_peers(dht, hex):
    peers = dht.get_peers(hex)
    return peers


if __name__ == "__main__":
    print("Initializing DHT", flush=True)
    dht = btdht.DHT()
    dht.start()  # now wait at least 15s for the dht to boostrap

    #  Ubuntu 16.10 Desktop (64-bit)
    hex = binascii.a2b_hex("0403fb4728bd788fbcb67e87d6feb241ef38c75a")
    peers = find_peers(hex)
    print('peers:', peers)
    exit(0)


