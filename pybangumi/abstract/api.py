"""
api类的抽象类模块 不可实例化 所有api类实现了该接口
"""
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

from pybangumi.abstract.data import InterfaceData


class AbstractAPI(metaclass=ABCMeta):
    """
    API抽象类
    """

    @property
    def url(self) -> str:
        return ''

    @abstractmethod
    def __init__(self):
        ...

    def __str__(self) -> str:
        return self.__request().__str__()

    def __repr__(self) -> str:
        return self.__request().__repr__()

    @abstractmethod
    def __request(self) -> dict:
        ...

    @abstractmethod
    def fetch(self) -> InterfaceData:
        ...
