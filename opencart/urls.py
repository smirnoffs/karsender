# -*- coding: utf-8 -*-
__author__ = 'Sergey Smirnov <smirnoffs@gmail.com>'
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'opencart.views.opencart_orders', name='opencart_orders'),
    url(r'^opencart/import_last_orders/$', 'opencart.views.import_last_orders', name='import_orders'),
]
