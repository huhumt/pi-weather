#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from get_weather import weather_info

def main():

    """
    this is the main entry of the project
    """

    forcast = weather_info("./config.json", "./city_list.json")
    weather_response = forcast.request_server()
    weather_parse = forcast.parse_weather(weather_response)
    weather_forcast = forcast.generate_weather_string(weather_parse)
    print(weather_forcast)

if __name__ == "__main__":
    main()
