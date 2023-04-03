# -*- coding: utf-8 -*-
"""
获取用户信息
"""
import requests

from pybangumi.abstract import AbstractAPI
from pybangumi.exceptions import UANotDefinedException, RequestFailedException
from .user_data import UserData


class User(AbstractAPI):
    """
    UserAPI
    \n
    Doc: https://bangumi.github.io/api/#/%E7%94%A8%E6%88%B7/getUserByName
    """

    def __init__(self, username: str, ua: str, timeout: int = 3600):
        self.__url = f"https://api.bgm.tv/user/{username}"
        self.__timeout = timeout
        if ua:
            self.__ua = ua
        else:
            raise UANotDefinedException()

    def _request(self) -> dict:
        r = requests.get(
            url=self.__url,
            headers={
                'User-Agent': self.__ua
            },
            timeout=self.__timeout
        )
        if r.status_code != 200:  # pragma: no cover
            r.raise_for_status()
        resp_json = r.json()
        try:
            if resp_json['code']:
                raise RequestFailedException(resp_json['error'])
        except KeyError:
            return resp_json

    def fetch(self) -> UserData:
        return UserData(self._request())

    @property
    def url(self):
        return self.__url
