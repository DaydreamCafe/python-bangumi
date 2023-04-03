# -*- coding: utf-8 -*-
"""
用于格式化输出数据类的函数 便于debug
"""
from pybangumi.abstract import AbstractData


def format_print(data: AbstractData, indent: int = 2):
    """
    格式化打印数据类
    :param data: 数据类实例
    :param indent: 缩进
    """
    data.format_print(print_indent=indent)
