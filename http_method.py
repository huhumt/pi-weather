#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request, parse

def http_get(url):

    """
    request website content using http get method
    """

    fd = request.urlopen(url)
    return fd.read().decode('utf-8')

def http_post(url, data_dict, headers):

    """
    request website content using http post method
    """

    data = parse.urlencode(data_dict).encode()
    req = request.Request(url=url, data=data, headers=headers)
    fd = request.urlopen(req)

    return fd.read()
