#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import asyncio
import btdht


# Вызывается, когда найдены участники сети DHT
def on_nodes_found(nodes):
    print("Найдены участники сети DHT:")
    for node in nodes:
        print(node)

# Основная функция для предоработки запроса и запуска поиска
async def find_dht_participants(search_query, num_results):
    # Генерируем уникальный идентификатор на основе поискового запроса
    search_query_bytes = search_query.encode()
    node_id = btdht.hash160(search_query_bytes)

    # Инициализируем клиент DHT
    client = btdht.DHTClient()
    dht_nodes = await client.bootstrap()

    # Ищем участников сети DHT
    found_nodes = await client.search(node_id, on_nodes_found)

    # Завершаем работу клиента DHT
    await client.close()

    return found_nodes[:num_results]

# Пример использования функции
query = "BitTorrent"
num_results = 3

loop = asyncio.get_event_loop()
results = loop.run_until_complete(find_dht_participants(query, num_results))

print("Результаты поиска:")
for result in results:
    print(result)
