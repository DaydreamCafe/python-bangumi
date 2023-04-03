# -*- coding: utf-8 -*-
"""
数据类型接口模块 所有api数据类型实现了该接口
"""
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from json import dumps
from typing import TypeVar, Union

TypeInterfaceData = TypeVar('TypeInterfaceData', bound='InterfaceData')


@dataclass
class AbstractData(metaclass=ABCMeta):  # pragma: no cover
    """
    数据类型接口 所有api数据类型实现了该接口
    """
    _data: Union[dict, list]

    @abstractmethod
    def __init__(self, _data: Union[dict, list]):
        self._data = _data
        ...

    def __repr__(self) -> str:
        return self._data.__repr__()

    def __str__(self) -> str:
        return self._data.__str__()

    def format_print(self, print_indent: int = 2):
        print(dumps(self._data, sort_keys=True, indent=print_indent, separators=(',', ':')))
