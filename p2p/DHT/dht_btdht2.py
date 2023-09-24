#!/usr/bin/env python3
# -*- coding: utf-8 -*-



import logging
import time
from btdht import DHT
import threading
import binascii


def dhtcrawler(selfaddr, bootaddr, bootinfo):
    MAX_WORKING_TIME = 60*10
    dht = DHT(bind_ip=selfaddr[0], bind_port=selfaddr[1])
    dht.start()
    dht.bootstrap(bootaddr[0], bootaddr[1])
    dht.ht.add_hash(bootinfo)
    time.sleep(MAX_WORKING_TIME)
    dht.stop()
    return


if __name__ == "__main__":

    # Enable logging
    loglevel = logging.INFO
    formatter = logging.Formatter("[%(levelname)s@%(created)s] %(message)s")
    stdout_handler = logging.StreamHandler()
    stdout_handler.setFormatter(formatter)
    logging.getLogger("btdht").setLevel(loglevel)
    logging.getLogger("btdht").addHandler(stdout_handler)

    logger = logging.getLogger(__name__)
    logger.setLevel(loglevel)
    logger.addHandler(stdout_handler)

    # CurrentMagnet = "746385fe32b268d513d068f22c53c46d2eb34a5c"
    CurrentMagnet = "4CDE5B50A8930315B479931F6872A3DB59575366"
    info_hash = binascii.a2b_hex(CurrentMagnet)
    threads = []
    threadNum = 3
    # dht.transmissionbt.com, 6881
    # 'router.utorrent.com', 6881
    for i in range(threadNum):
        t = threading.Thread(target=dhtcrawler, args=(("0.0.0.0", 60000 + i), ('router.bittorrent.com', 6881), info_hash))
        threads.append(t)

    for thread in threads:
        thread.start()
        time.sleep(2)


    # Find me peers for that torrent hashes
    # dht.ht.add_hash(CurrentMagnet.decode("hex"))
    # TotalCnt = 0
    # Res = []
    # for count in xrange(4):
    #     logger.info("DHT Nodes found: %d" % (dht.rt.count()))
    #     logger.info("Bad DHT nodes found: %d" % (dht.rt.bad_count()))
    #     logger.info("Total peers found: %d" % (dht.ht.count_all_peers()))
    #
    #     # How many peers at this moment?
    #     peers = dht.ht.get_hash_peers(CurrentMagnet.decode("hex"))
    #     for peer in peers:
    #         TotalCnt += 1
    #         Res.append((peer))
    #         logger.info("Found peer: %s:%d" % (peer))
    #     time.sleep(3)
    # logger.info("Found peers (total): %d" % (TotalCnt))
    # logger.info("Found peers (uniq): %d" % (len(set(Res))))
    # dht.stop()



