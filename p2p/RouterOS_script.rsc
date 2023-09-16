#!/usr/bin/env bash
# -*- coding: utf-8 -*-


/ip firewall address-list
add address=bt.t-ru.org  comment=bt  list=BitTorrentTrackers
add address=bt2.t-ru.org comment=bt2 list=BitTorrentTrackers
add address=bt3.t-ru.org comment=bt3 list=BitTorrentTrackers
add address=bt4.t-ru.org comment=bt4 list=BitTorrentTrackers


/ip firewall nat add
dst-address-list=BitTorrentTrackers log=yes log-prefix="BitTorrentTrackers" chain=dstnat protocol=tcp dst-port=80 action=dst-nat to-ports=80

