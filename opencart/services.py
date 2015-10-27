# -*- coding: utf-8 -*-
import logging

from pymongo.errors import BulkWriteError

from karsender.database import get_collection
from .database import session

__author__ = 'Sergey Smirnov <smirnoffs@gmail.com>'

import datetime
import pymongo
from .database import Order

logging.basicConfig(filename='opencart.log', level=logging.INFO, format="%(asctime)s : %(levelname)s : %(message)s")


def get_last_success_import():
    last_import = get_collection('status').find({'success': True}).sort('datetime', pymongo.DESCENDING).limit(1)
    if not last_import.count():
        return datetime.datetime(year=1980, month=1, day=1)
    return last_import[0]['datetime']


def set_last_import_status(success=False, time=None):
    if not time:
        time = datetime.datetime.now()
    get_collection('status').insert_one({'success': success, 'datetime': time})


def get_last_orders():
    last_import = get_last_success_import()
    logging.info('Queering new orders')
    orders_to_import = session.query(Order).filter(Order.date_added > last_import)
    order_count = orders_to_import.count()
    logging.info('{order_count} orders to import'.format(order_count=order_count))
    collection = get_collection()
    if order_count:
        try:
            collection.insert_many([{'_id': order.order_id,
                                 'firstname': order.firstname,
                                 'lastname': order.lastname,
                                 'email': order.email,
                                 'telephone': order.telephone,
                                 'shipping_city': order.shipping_city,
                                 'shipping_zone': order.shipping_zone,
                                 'total': float(order.total),
                                 'date': order.date_added,
                                 } for order in orders_to_import])
        except BulkWriteError as e:
            if e.details['writeErrors'][0]['code'] == 11000:
                logging.error('Duplicated order ids')
    logging.info("{order_count} orders imported from opencart to karsender".format(order_count=order_count))
    set_last_import_status(success=True)
