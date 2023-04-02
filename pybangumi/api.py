# -*- coding: utf-8 -*-
"""
api模块
"""
from pybangumi.user import User


class BangumiAPI:
    """
    API类
    """
    def __init__(self, ua: str, timeout: int = 3600):
        self.ua = ua
        self.timeout = timeout

    def new_user(self, username: str):
        return User(username, self.ua, self.timeout)
