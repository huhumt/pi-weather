#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request, parse

def http_get(url):

    """
    request website content using http get method
    """

    fd = request.urlopen(url)
    return fd.read().decode()

def http_post(url, data_dict):

    """
    request website content using http post method
    """

    req =  request.Request(url, data=parse.urlencode(data_dict).encode())
    fd = request.urlopen(req)

    return fd.read()
