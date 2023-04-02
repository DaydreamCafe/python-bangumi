# -*- coding: utf-8 -*-
"""
用户信息返回值dataclass
"""
from dataclasses import dataclass
from typing import TypeVar

from pybangumi.abstract.data import InterfaceData


TypeAvatarData = TypeVar('TypeAvatarData', bound='AvatarData')
TypeUserData = TypeVar('TypeUserData', bound='UserData')


@dataclass
class AvatarData(InterfaceData):
    large: str = ''
    medium: str = ''
    small: str = ''

    def init(self, avatar: dict) -> TypeAvatarData:
        self.large = avatar['large']
        self.medium = avatar['medium']
        self.small = avatar['small']
        return self


@dataclass
class UserData(InterfaceData):
    avatar: AvatarData = AvatarData()
    sign: str = ''
    username: str = ''
    nickname: str = ''
    id: int = -1
    usergroup: int = -1

    def init(self, user: dict) -> TypeUserData:
        self.avatar = AvatarData().init(user['avatar'])
        self.sign = user['sign']
        self.username = user['username']
        self.nickname = user['nickname']
        self.id = user['id']
        self.usergroup = user['usergroup']
        return self
