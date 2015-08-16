# -*- coding: utf-8 -*-
import os

__author__ = 'Sergey Smirnov <smirnoffs@gmail.com>'


class Config:
    OPENCART_DB_HOST = os.getenv('OPENCART_DB_HOST')
    OPENCART_DB_PORT = os.getenv('OPENCART_DB_PORT', 3306)
    OPENCART_DB_USER = os.getenv('OPENCART_DB_USER')
    OPENCART_DB_PSWR = os.getenv('OPENCART_DB_PSWR')
    OPENCART_DB_DATABASE = os.getenv('OPENCART_DB_DATABASE')

    MONGO_DB_HOST = os.getenv('MONGO_DB_HOST', 'localhost')
    MONGO_DB_DATABASE = os.getenv('MONGO_DB_DATABASE', 'karsend')
    ORDERS_COLLECTION = 'orders'