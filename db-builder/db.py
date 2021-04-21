"""
    db.py
    Tom Amaral <thomasamaral2016@gmail.com>

    A (very simple) python module to build a mongodb collection based off the
    web scraping results from scrape.py
"""

import pymongo
from scrape import get_kanto

MONGO_CLIENT = pymongo.MongoClient("mongodb://localhost:27017/")
POKE_DB = MONGO_CLIENT["pokedex"]
POKE_COLLECTION = POKE_DB["pokemon"]


if __name__ == "__main__": 
    kanto_objects = get_kanto()
    result = POKE_COLLECTION.insert_many(kanto_objects)
    print(f'Inserted {len(result.inserted_ids)} entries into the Pokedex collection')
