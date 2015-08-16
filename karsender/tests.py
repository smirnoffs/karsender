# -*- coding: utf-8 -*-
from karsender.database import get_collection
from karsender.services import validate_emails

__author__ = 'Sergey Smirnov <smirnoffs@gmail.com>'
from unittest import TestCase


class TestServices(TestCase):
    def test_validate_emails(self):
        validate_emails()