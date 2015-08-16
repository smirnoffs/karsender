# -*- coding: utf-8 -*-
__author__ = 'Sergey Smirnov <smirnoffs@gmail.com>'

import datetime

import pymongo

from karsender.config import Config


def get_collection():
    client = pymongo.MongoClient(Config.MONGO_DB_HOST)
    db = client[Config.MONGO_DB_DATABASE]
    return db[Config.ORDERS_COLLECTION]


def get_last_success_import():
    last_import = get_collection().find({'success': True}).sort('datetime', pymongo.DESCENDING).limit(1)
    if not last_import.count():
        return datetime.datetime(year=1980, month=1, day=1)
    return last_import[0]['datetime']


def get_last_orders():
    last_import = get_last_success_import()
