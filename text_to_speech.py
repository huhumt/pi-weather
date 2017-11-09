#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from http_method import http_get, http_post
import json

def tts_engine(config_file, input_string):

    """
    use voicerss.org to do text_to_speech
    http://api.voicerss.org/?<parameters>
    """

    base_url = "https://api.voicerss.org/"

    # read config file for key
    fd = open(config_file, 'r')
    config = json.load(fd)
    fd.close()

    # get key
    api_key = config['tts_key']

    # generate http get url
    url = base_url
    # add key information
    url += ("?key=" + api_key)
    # choose language
    url += ("&hl=en-au")
    # choose speech rate, -10 to 10
    url += ("&r=-1")
    # add text need to transfer
    url += ("&src=" + input_string)

    print(url)

    # support both http get and http post
    headers = {
            "User-Agent":"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11",
            "Content-Type": "application/x-www-form-urlencoded"
            }
    response = http_post(url, headers)

    # write data into file
    fd = open("./weather_forecast.mp3", 'wb')
    fd.write(response)
    fd.close()
