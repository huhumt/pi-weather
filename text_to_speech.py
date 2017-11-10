#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from http_method import http_get, http_post
import json

def tts_engine_voicerss(config_file, input_string):

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

    data_dict = {
            "key":api_key,            # api key
            "hl":"en-us",             # language
            "r":-2,                   # speech speed, -10~10
            "c":"WAV",                # codec, can be MP3, WAV, OGG
            "f":"44khz_16bit_mono",   # sample rate
            "src":input_string        # text need to be transfered
            }

    # support both http get and http post
    headers = {
            "User-Agent":"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11",
            "Content-Type": "application/x-www-form-urlencoded"
            }
    response = http_post(base_url, data_dict, headers)

    # write data into file
    fd = open("./weather_forecast.mp3", 'wb')
    fd.write(response)
    fd.close()

def tts_engine_ibm(config_file, input_string):

    '''
    This is text_to_speech engine supported by IBM
    https://stream.watsonplatform.net/text-to-speech/api/v1/synthesize
    '''

    base_url = "https://stream.watsonplatform.net/text-to-speech/api/v1/synthesize"

    # read username and password from config file
    fd = open(config_file, 'r')
    config = json.load(fd)
    fd.close()

    # get api username and password
    username = config['tts_username']
    password = config['tts_password']

    # generate data dictionary
    data_dict = {
            "Content-Type":"application/json",
            "accept":"audio/flac",                # audio format
            "voice":"en-US_MichaelVoice"
            }
