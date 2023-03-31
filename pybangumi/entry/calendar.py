"""
每日放送
"""

# -*- coding: utf-8 -*-
import requests

from pybangumi.basic.const import headers


class Calendar:
    def __init__(self):
        self.__url = "https://api.bgm.tv/calendar"

    def __str__(self):
        return self.__request().__str__()

    def __repr__(self):
        return self.__request().__repr__()

    def __request(self) -> list:
        result = requests.get(url=self.__url, headers=headers)
        return result.json()

    def get(self) -> list:
        return self.__request()

    @property
    def url(self):
        return self.__url
