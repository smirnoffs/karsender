# -*- coding: utf-8 -*-
from .config import Config

__author__ = 'Sergey Smirnov <smirnoffs@gmail.com>'

from flask import Flask


app = Flask(__name__)
app.config.from_object(Config)