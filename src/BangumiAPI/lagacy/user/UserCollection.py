"""
获取用户收藏信息
Warning: 这是一个已经被弃用的API，尽管它目前仍然可以使用，但是这么做是不推荐的，因为它随时可能不能再继续使用
您应该使用BangumiAPI.User.UserCollections来取代它
"""

# -*- coding: utf-8 -*-
import requests


class UserCollection:
    def __init__(self, username: str, category: str = 'watching', ids: list = None, response_group: str = 'medium'):
        """
        获取用户收藏信息

        :param username: 用户名或UID
        :param category: 收藏类型
                         watching = 在看的动画与三次元条目
                         all_watching = 在看的动画三次元与书籍条目
                         默认为 watching
        :param ids: 收藏条目 ID
                    批量查询收藏状态，如 [1, 2, 4, 6]
        :param response_group: medium / small
                               默认为 medium, small 时不返回条目详细信息
        """
        self.__response_group = response_group
        self.__category = category
        match ids:
            case None:
                self.__ids = None
                self.__params = {
                    'cat': self.__category,
                    'response_group': self.__response_group
                }
            case _:
                self.__ids = ''
                for i in ids:
                    self.__ids += f'{i},'
                self.__ids = self.__ids[:-1]
                self.__params = {
                    'cat': self.__category,
                    'response_group': self.__response_group,
                    'ids': self.__ids
                }

        self.__url = f'https://api.bgm.tv/user/{username}/collection'

    def __str__(self):
        return self.__request().__str__()

    def __repr__(self):
        return self.__request().__repr__()

    def __request(self) -> dict:

        r = requests.get(self.__url, params=self.__params)
        if r.status_code != 200:
            r.raise_for_status()
        return r.json()

    def get(self) -> dict:
        return self.__request()

    @property
    def url(self):
        return self.__url

    @property
    def ids(self):
        return self.__ids

    @property
    def request_param(self):
        return self.__params

    @property
    def response_group(self):
        return self.__response_group

    @property
    def category(self):
        return self.__category


if __name__ == '__main__':
    print(UserCollection('sai'))
