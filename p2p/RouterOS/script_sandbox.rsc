#!/usr/bin/env bash
# -*- coding: utf-8 -*-


/ip firewall address-list
add address=bt.t-ru.org comment=bt list=BitTorrentTrackers
add address=bt2.t-ru.org comment=bt2 list=BitTorrentTrackers
add address=bt3.t-ru.org comment=bt3 list=BitTorrentTrackers
add address=bt4.t-ru.org comment=bt4 list=BitTorrentTrackers


/ip firewall nat
add dst-address-list=BitTorrentTrackers log=yes log-prefix="BitTorrentTrackers" chain=dstnat protocol=tcp dst-port=80 action=dst-nat to-ports=80


/ip dns static
add name=my_retracker1.local cname=tracker.dler.org
add name=my_retracker1.local cname=tracker.files.fm
add name=my_retracker2.local cname=tracker.lilithraws.org
add name=my_retracker2.local cname=tracker.loligirl.cn


#my_retracker1.local:6969/announce
#tracker.dler.org:6969/announce
#tracker.files.fm:6969/announce

#https://my_retracker1.local:6969/announce
#https://tracker.lilithraws.org:443/announce
#https://tracker.loligirl.cn:443/announce

