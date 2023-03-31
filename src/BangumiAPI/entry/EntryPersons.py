"""
获取条目Staff
"""

# -*- coding: utf-8 -*-
import requests


class EntryPersons:
    def __init__(self, subject_id: (str | int)):
        self.__url = f"https://api.bgm.tv/v0/subjects/{subject_id}/persons"

    def __str__(self):
        return self.__request().__str__()

    def __repr__(self):
        return self.__request().__repr__()

    def __request(self) -> dict:
        r = requests.get(url=self.__url, headers=headers)
        if r.status_code != 200:
            r.raise_for_status()
        return r.json()

    def get(self) -> dict:
        return self.__request()

    @property
    def url(self):
        return self.__url


if __name__ == "__main__":
    print(EntryPersons(326868))
