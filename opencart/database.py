# -*- coding: utf-8 -*-
__author__ = 'Sergey Smirnov <smirnoffs@gmail.com>'

from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base

from sqlalchemy.orm import Session
from flask.ext.sqlalchemy import SQLAlchemy

from karsender import Config

__author__ = 'Sergey Smirnov <smirnoffs@gmail.com>'

db = SQLAlchemy()
engine = create_engine('mysql+pymysql://{user}:{password}@{server}/{db}?charset=utf8'.format(
    user=Config.OPENCART_DB_USER,
    password=Config.OPENCART_DB_PSWR,
    server=Config.OPENCART_DB_HOST,
    db=Config.OPENCART_DB_DATABASE,
), pool_recycle=3600)

Base = automap_base()

Base.prepare(engine, reflect=True)

# mapped classes are now created with names by default
# matching that of the table name.
Order = Base.classes.oc_order

session = Session(engine)
