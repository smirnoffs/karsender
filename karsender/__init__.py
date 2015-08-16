# -*- coding: utf-8 -*-
import logging

from .config import Config

__author__ = 'Sergey Smirnov <smirnoffs@gmail.com>'

from flask import Flask

logging.basicConfig(filename='karsender.log', level=logging.INFO, format="%(asctime)s : %(levelname)s : %(message)s",
                    filemode='w')
logger = logging.getLogger()

app = Flask(__name__)
app.config.from_object(Config)
