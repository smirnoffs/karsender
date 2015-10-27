# -*- coding: utf-8 -*-
from django.core.urlresolvers import resolve, reverse_lazy
from django.shortcuts import render, redirect
from pymongo import DESCENDING

from karsender.database import get_collection
from .services import get_last_success_import, get_last_orders

__author__ = 'Sergey Smirnov <smirnoffs@gmail.com>'


def opencart_orders(request):
    last_import_date = get_last_success_import()
    collection = get_collection()
    orders_imported = collection.count()
    last_imported = tuple(collection.find().sort("_id", DESCENDING).limit(5))
    for order in last_imported:
        order['order_number'] = order['_id']
    return render(request, "opencart/orders.html", {"last_import_date": last_import_date,
                                                        "last_import_date_iso": last_import_date.isoformat(),
                                                        "orders_imported": orders_imported,
                                                        "last_imported": last_imported})


def import_last_orders(request):
    get_last_orders()
    return redirect(reverse_lazy('opencart:opencart_orders'))
