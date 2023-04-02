# -*- coding: utf-8 -*-
"""
用户信息返回值dataclass
"""
from dataclasses import dataclass, field
from typing import TypeVar

from pybangumi.abstract import InterfaceData


TypeAvatarData = TypeVar('TypeAvatarData', bound='AvatarData')
TypeUserData = TypeVar('TypeUserData', bound='UserData')


@dataclass
class AvatarData(InterfaceData):
    """
    头像dataclass
    """
    large: str
    medium: str
    small: str

    def __init__(self, data: dict):
        self.large = data['large']
        self.medium = data['medium']
        self.small = data['small']


@dataclass
class UserData(InterfaceData):
    """
    用户信息dataclass
    """
    avatar: AvatarData
    sign: str
    username: str
    nickname: str
    userid: int
    usergroup: int

    def __init__(self, data: dict):
        self.avatar = AvatarData(data['avatar'])
        self.sign = data['sign']
        self.username = data['username']
        self.nickname = data['nickname']
        self.userid = data['id']
        self.usergroup = data['usergroup']
