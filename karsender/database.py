# -*- coding: utf-8 -*-
import pymongo

from karsender import Config

__author__ = 'Sergey Smirnov <smirnoffs@gmail.com>'


def get_collection(collection='orders'):
    collections = {'orders': Config.ORDERS_COLLECTION,
                   'status': Config.STATUSES_COLLECTION,
                   'customers': Config.CUSTOMERS_COLLECTION,}
    client = pymongo.MongoClient(Config.MONGO_DB_HOST)
    db = client[Config.MONGO_DB_DATABASE]
    return db[collections[collection]]
