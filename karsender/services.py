# -*- coding: utf-8 -*-
import DNS

from .database import get_collection

from . import logger

__author__ = 'Sergey Smirnov <smirnoffs@gmail.com>'

MX_DNS_CACHE = {}


def get_mx_ip(mx_host):
    """
    Get the IP address of a given MX host

    :param mx_host: The host being looked up
    :type mx_host: str
    :return: A list of IP addresses
    :rtype: list
    """
    if mx_host not in MX_DNS_CACHE:
        try:
            MX_DNS_CACHE[mx_host] = DNS.mxlookup(mx_host)
        except DNS.Base.ServerError as e:
            if e.rcode == 3:  # NXDOMAIN (Non-Existent Domain)
                MX_DNS_CACHE[mx_host] = None
            else:
                raise
    return MX_DNS_CACHE[mx_host]


def validate_email(email):
    hostname = email[email.find('@') + 1:]
    mx_hosts = get_mx_ip(hostname)
    if mx_hosts:
        return True
    return False


def validate_emails():
    collection = get_collection()
    logger.info("Getting non validated emails")
    for order in collection.find({'email_validated': {"$exists": False}}):
        email = order['email']
        is_valid = validate_email(email)
        order['email_validated'] = True
        order['email_valid'] = is_valid
        collection.save(order)
        logger.info('{email} is {result}'.format(email=email, result='valid' if is_valid else 'non valid'))


def copy_valid_opencart_customers():
    emails = get_collection('orders').distinct('email').find({'email_valid': True})
    for email in emails:
        customer = {}
        orderN