# -*- coding: utf-8 -*-
"""
api类的抽象类模块 不可实例化 所有api类实现了该抽象类
"""
from abc import ABCMeta, abstractmethod

from .data import AbstractData


class AbstractAPI(metaclass=ABCMeta):  # pragma: no cover
    """
    API抽象类
    """

    @property
    def url(self) -> str:
        return ''

    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    def _request(self):
        ...

    @abstractmethod
    def fetch(self) -> AbstractData:
        ...

    def __str__(self) -> str:
        return self._request().__str__()

    def __repr__(self) -> str:
        return self._request().__repr__()
