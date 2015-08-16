# -*- coding: utf-8 -*-
__author__ = 'Sergey Smirnov <smirnoffs@gmail.com>'

import pymongo
from karsender.config import Config

client = pymongo.MongoClient(Config.MONGO_DB_HOST)
db = client[Config.MONGO_DB_DATABASE]
collection= db[Config.ORDERS_COLLECTION]

def get_last_success_import():
    last_import = collection.find_one(success=True).sort('datetime')


def get_last_orders():
