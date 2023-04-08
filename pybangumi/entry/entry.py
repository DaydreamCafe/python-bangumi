"""
获取条目
"""

# -*- coding: utf-8 -*-
import requests

from pybangumi.consts.__init__ import headers


class Entry:
    def __init__(self, subject_id: (str | int)):
        self.__url = f"https://api.bgm.tv/v0/subjects/{subject_id}"

    def __str__(self):
        return self.__request().__str__()

    def __repr__(self):
        return self.__request().__repr__()

    def __request(self) -> dict:
        result = requests.get(url=self.__url, headers=headers)
        if result.status_code != 200:
            result.raise_for_status()
        return result.json()

    def fetch(self) -> dict:
        return self.__request()

    @property
    def url(self):
        return self.__url
