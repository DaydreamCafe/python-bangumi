# -*- coding: utf-8 -*-
"""
获取用户信息
"""
import requests

from pybangumi.consts import headers
from pybangumi.abstract.api import AbstractAPI
from pybangumi.user.user_data import UserData


class User(AbstractAPI):
    def __init__(self, username: str):
        self.__url = f"https://api.bgm.tv/user/{username}"

    def _request(self) -> dict:
        r = requests.get(url=self.__url, headers=headers)
        if r.status_code != 200:
            r.raise_for_status()
        return r.json()

    def fetch(self) -> UserData:
        return UserData().init(self._request())

    @property
    def url(self):
        return self.__url


if __name__ == "__main__":
    print(User("653154").fetch())
