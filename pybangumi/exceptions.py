# -*- coding: utf-8 -*-
"""
错误
"""


class UANotDefinedException(Exception):
    """
    UA未定义错误
    """
    def __init__(self):
        super().__init__('UA not defined')
