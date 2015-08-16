# -*- coding: utf-8 -*-
__author__ = 'Sergey Smirnov <smirnoffs@gmail.com>'

import unittest


class TestOrderExport(unittest.TestCase):
    def test_get_last_orders(self):
        orders = get_last_orders()
        self.assertIsNotNone(orders)
        self.assertGreater(len(orders), 0)
        self.assertTrue(all(isinstance(order, Order) for order in orders))
