# -*- coding: utf-8 -*-
import datetime
from unittest.mock import patch

from karsender import Config

from opencart.services import get_last_success_import, get_last_orders
from karsender.database import get_collection

__author__ = 'Sergey Smirnov <smirnoffs@gmail.com>'

import unittest


class MockConfig(Config):
    ORDERS_COLLECTION = 'test_collection'


mock = patch.object(Config, 'ORDERS_COLLECTION', 'test_collection')


class TestOrderExport(unittest.TestCase):
    def test_get_last_orders(self):
        orders = get_last_orders()
        # self.assertIsNotNone(orders)
        # self.assertGreater(len(orders), 0)
        # self.assertTrue(all(isinstance(order, Order) for order in orders))

    def setUp(self):
        mock.start()
        self.collection = get_collection()

    def test_get_last_success_import(self):
        last_import = get_last_success_import()
        self.assertIsInstance(last_import, datetime.datetime)
        self.assertEqual(last_import, datetime.datetime(year=1980, month=1, day=1))
        success_date = datetime.datetime(year=2014, month=2, day=12, hour=12, minute=4, second=14)
        self.collection.insert_one({'success': True, 'datetime': success_date})
        self.collection.insert_one({'success': False, 'datetime': datetime.datetime.now()})
        self.assertIsInstance(last_import, datetime.datetime)
        self.assertEqual(get_last_success_import(), success_date)

    def tearDown(self):
        self.collection.drop()
        mock.stop()