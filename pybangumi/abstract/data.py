"""
数据类型接口模块 所有api数据类型实现了该接口
"""
# -*- coding: utf-8 -*-
from typing import Union, TypeVar
from dataclasses import dataclass
from abc import ABCMeta


TypeInterfaceData = TypeVar('TypeInterfaceData', bound='InterfaceData')


@dataclass
class InterfaceData(metaclass=ABCMeta):
    """
    数据类型接口 所有api数据类型实现了该接口
    """
    ...
