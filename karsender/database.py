# -*- coding: utf-8 -*-
import pymongo
from karsender import Config

__author__ = 'Sergey Smirnov <smirnoffs@gmail.com>'


def get_collection():
    client = pymongo.MongoClient(Config.MONGO_DB_HOST)
    db = client[Config.MONGO_DB_DATABASE]
    return db[Config.ORDERS_COLLECTION]