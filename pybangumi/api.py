# -*- coding: utf-8 -*-
"""
api模块
"""
from pybangumi.consts import TIMEOUT, USER_AGENT
from pybangumi.entry import Entry
from pybangumi.user import User


class BangumiAPI:
    """
    API类
    """

    def __init__(self, ua: str = USER_AGENT, timeout: int = TIMEOUT):
        self.ua = ua
        self.timeout = timeout

    def new_user(self, username: str):
        return User(username, self.ua, self.timeout)

    def new_entry(self, subject_id: (str | int)):
        return Entry(subject_id)
