# -*- coding: utf-8 -*-
"""
用于获取构造后的API URL的函数
"""
from pybangumi.abstract import AbstractAPI


def get_url(api_instance: AbstractAPI) -> str:
    """
    获取一个API实例的请求URL
    :param api_instance: API实例
    :return: 构造后的请求URL
    """
    return api_instance.url
