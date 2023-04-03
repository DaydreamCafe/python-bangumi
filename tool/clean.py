# -*- coding: utf-8 -*-
"""
清理构建文件
"""
import os


def clean_dist():
    """
    清理构建文件的函数
    """
    os.chdir("dist")
    file_list = os.listdir(os.getcwd())
    for file in file_list:
        os.remove(file)
    os.chdir("..")
    os.rmdir("dist")
