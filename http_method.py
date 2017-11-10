#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request, parse

def http_get(url):

    """
    request website content using http get method
    """

    fd = request.urlopen(url)
    length = fd.getheader('Content-Length')

    return fd.read().decode('utf-8')

def http_post(url, data_dict, headers):

    """
    request website content using http post method
    """

    data = parse.urlencode(data_dict).encode()
    req = request.Request(url=url, data=data, headers=headers)
    fd = request.urlopen(req)
    length = fd.getheader('Content-Length')

    return fd.read()

def http_auth(url, username, password):
    # Create an OpenerDirector with Basic HTTP Authentication...
    auth_handler = request.HTTPBasicAuthHandler()
    auth_handler.add_password(
            realm='PDQ Application',
            uri=url,
            user=username,
            passwd=password)
    opener = request.build_opener(auth_handler)
    # ...and install it globally so it can be used with urlopen.
    request.install_opener(opener)
