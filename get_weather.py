#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from http_method import http_get, http_post
from get_date_time import get_date, get_time
import json

class weather_info:

    """
    get weather information using api:
        http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID={APIKEY}
        where: id represents city, and APPID is user identification
    """

    def __init__(self, config_file, city_id):

        '''
        read config file and search for city id
        '''

        # generate weather forecast url based on city
        self.city = ''
        self.city_id = ''
        # appid for authorization
        self.appid = ''

        # open file descriptor
        fd1 = open(config_file, 'r', encoding="utf-8")
        fd2 = open(city_id, 'r', encoding="utf-8")
        try:
            # load file as json format
            config_data = json.load(fd1)
            city_data = json.load(fd2)

            # get config city in capital and remove all the whitespace
            self.city = (config_data['city'].upper()).replace(' ', '')
            # get country and appid
            config_country = config_data['country'].upper()
            self.appid = config_data['weather_appid']

            # find city id based on config city
            for data in city_data:
                # search for city id based on name
                city = (data['name'].upper()).replace(' ', '')
                country = data['country'].upper()

                # config city id found, to avoid same city name in
                # different country, we use country code here
                if config_country == country and self.city == city:
                    self.city_id = data['id']
                    break
                # use Newport, Melbourne, Austrilia default
                else:
                    self.city_id = '2155411'
        finally:
            fd1.close()
            fd2.close()

    def request_server(self):

        '''
        request server for weather information
        '''

        # generate weather request url
        base_url = 'http://api.openweathermap.org/data/2.5/forecast'
        url = base_url + '?'
        url += ('id=' + str(self.city_id))
        url += ('&units=metric')
        url += ('&APPID=' + self.appid)

        # use http get information
        response = http_get(url)

        return response

    def parse_weather(self, response):

        '''
        parse useful information from the long json file
        '''

        weather_data = json.loads(response)
        daylight_keys = ['morning', 'noon', 'afternoon', 'night']
        daylight = {
                'morning':'09:00:00',      # in the lovely morning
                'noon':'12:00:00',         # lunch time
                'afternoon':'15:00:00',    # afternoon tea
                'night':'21:00:00'         # sleep on bed
                }
        weather_output = {
                'daylight':'',     # moring, noon, afternoon or night
                'weather_main':'', # sunny, cloudy etc.
                'humidity':'',     # humidity
                'temperature':'',  # temperature
                'wind_speed':'',   # wind speed
                'wind_deg':''      # wind direction
                }

        # get system date
        cur_date = get_date()

        # create a weather list
        weather_list = []

        # report moring, noon, afternoon and night
        for cur_time in daylight_keys:
            cur_date_time = cur_date + ' ' + daylight[cur_time]
            # search for useful information
            for tmp_dict in weather_data['list']:
                # only report today's weather
                if cur_date_time == tmp_dict['dt_txt']:
                    # update useful weather information
                    weather_output['daylight'] = cur_time
                    weather_output['weather_main'] = (tmp_dict['weather'][0])['main']
                    weather_output['humidity'] = tmp_dict['main']['humidity']
                    weather_output['temperature'] = tmp_dict['main']['temp']
                    weather_output['wind_speed'] = tmp_dict['wind']['speed']
                    weather_output['wind_deg'] = tmp_dict['wind']['deg']
                    weather_list.append(weather_output.copy())
                    break

        return weather_list

    def generate_weather_string(self, weather_list):

        '''
        generate a weather string for tts engine
        '''

        output_string = "Today is " + get_date()
        output_string += (", and now it's " + get_time())
        output_string += (". Play weather forcast in " + self.city + ".")
        play_once_flag = False
        # generate morning, noon, afternoon, night weather report
        for tmp_dict in weather_list:
            if tmp_dict['daylight'] == "night":
                output_string += " At night"
            else:
                output_string += (" In the " + tmp_dict['daylight'])
            output_string += (", it's " + tmp_dict['weather_main'])
            output_string += (", the temperature is " + str(tmp_dict['temperature']) + " degree")

            # add some tips
            if not play_once_flag:
                if tmp_dict['weather_main'] == "Rain":
                    output_string += ". Don't forget to take a umbrella"
                    play_once_flag = True
                else:
                    output_string += ". Wish you have a nice day"
                    play_once_flag = True

            output_string += (". The wind speed is " + str(tmp_dict['wind_speed']) + " meter per second")
            output_string += (", the humidity is " + str(tmp_dict['humidity']) + " percent.")

        # finish weather forecast, now listen to radio
        output_string += ("Now let's enjoy some radio.")

        return output_string
