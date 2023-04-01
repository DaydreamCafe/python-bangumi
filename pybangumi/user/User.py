"""
获取用户信息
"""

# -*- coding: utf-8 -*-
import requests

from pybangumi.consts import headers
from pybangumi.abstract.api import AbstractAPI


class User(AbstractAPI):
    def __init__(self, username: str):
        self.__url = f"https://api.bgm.tv/user/{username}"

    def __str__(self):
        return self.__request().__str__()

    def __repr__(self):
        return self.__request().__repr__()

    def __request(self) -> dict:
        r = requests.get(url=self.__url, headers=headers)
        if r.status_code != 200:
            r.raise_for_status()
        return r.json()

    def fetch(self) -> dict:
        return self.__request()

    @property
    def url(self):
        return self.__url


if __name__ == "__main__":
    print(User("653154"))
