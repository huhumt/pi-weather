#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime, date

"""
get system time and date
"""

def get_time():

    '''
    get current time
    '''

    today = datetime.today()
    hour = str(today.strftime("%H"))
    minute = str(today.strftime("%M"))

    return hour + ":" + minute

def get_date():

    '''
    get current date
    '''

    cur_date = date.today()

    return str(cur_date)

def get_weekday():

    '''
    get weekday number
    '''

    return str(datetime.today().strftime("%A"))
