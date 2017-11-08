#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from http_method import http_get, http_post
import json

class auth_method:

    """
    an implementation for yahoo auth2
    """

    def __init__(self, filename):

        '''
        read config file
        '''

        # generate weather forecast url based on location
        self.location = ''
        self.temp_unit = ''
        # public_key and secret_key for authorization
        self.public_key = ''
        self.secret_key = ''

        fd = open(filename, 'r')
        try:
            config_data = json.load(fd)
            self.location = config_data['location']
            self.temp_unit = config_data['unit']
            self.public_key = config_data['client_id']
            self.secret_key = config_data['client_secret']
        finally:
            fd.close()

    def request_server(self):

        '''
        generate a re-direct url and request the server
        '''

        oauth2_url = 'https://api.login.yahoo.com/oauth2/request_auth'
        client_id = self.public_key
        redirect_uri = 'https://weather-ydn-yql.media.yahoo.com/forecastrss'
        lang = 'en-us'

        # load location information from config file
        if self.location:
            redirect_uri += ('?w=' + self.location)
        # display temprature in Sunnyvale, Californion in default
        else:
            redirect_uri += '?w=2442047'

        # use Celsius or Fahrenheit as temprature unit
        if self.temp_unit == 'Celsius':
            redirect_uri += '&u=c'
        # use Fahrenheit as default
        else:
            redirect_uri += '&u=f'

        output_url = oauth2_url + '?'
        output_url += ('client_id=' + client_id)
        output_url += ('&redirect_uri=' + redirect_uri)
        output_url += '&response_type=code'
        output_url += ('&language=' + lang)

        print(output_url)

        # support HTTP GET and HTTP POST here
        resp = http_get(output_url)
        print(resp)
        fd = open('./test.log', 'w')
        fd.write(resp)
        fd.close()

    def auth_server(self):

        '''
        authorized to server
        '''

        self.request_server()
