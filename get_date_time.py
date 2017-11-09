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

    # get current date and time
    cur_datetime = datetime.now()

    # get hour, minute, second
    hour = cur_datetime.hour
    if hour < 10:
        hour = '0' + str(hour)
    else:
        hour = str(hour)

    minute = cur_datetime.minute
    if minute < 10:
        minute = '0' + str(minute)
    else:
        minute = str(minute)

    second = cur_datetime.second
    if second < 10:
        second = '0' + str(second)
    else:
        second = str(second)

    # format current time
    cur_time = hour + ':' + minute + ':' + second

    return cur_time

def get_date():

    '''
    get current date
    '''

    cur_date = date.today()

    return str(cur_date)
