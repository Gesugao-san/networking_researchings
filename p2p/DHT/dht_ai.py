#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import asyncio
from dht import DHT

async def find_peers():
    # Создаем экземпляр DHT
    dht = DHT()

    # Запускаем DHT
    await dht.listen(6881)

    # Ключ, по которому будем искать информацию в DHT
    info_hash = b'YOUR_INFO_HASH_HERE'

    # Ищем пиры для заданного info_hash
    peers = await dht.get_peers(info_hash)

    # Выводим найденные пиры
    for peer in peers:
        print(f"Найден пир: {peer}")

    # Останавливаем DHT
    await dht.stop()

if __name__ == "__main__":
    asyncio.run(find_peers())



