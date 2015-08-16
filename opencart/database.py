# -*- coding: utf-8 -*-
__author__ = 'Sergey Smirnov <smirnoffs@gmail.com>'

from flask.ext.sqlalchemy import SQLAlchemy, Model
from sqlalchemy import create_engine

from karsender import Config

__author__ = 'Sergey Smirnov <smirnoffs@gmail.com>'

db = SQLAlchemy()
engine = create_engine('mysql+pymysql://{user}:{password}@{server}/{db}'.format(
    user=Config.OPENCART_DB_USER,
    password=Config.OPENCART_DB_PSWR,
    server=Config.OPENCART_DB_HOST,
    db=Config.OPENCART_DB_DATABASE,
), pool_recycle=3600)
