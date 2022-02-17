# -*- coding: utf-8 -*-
import setuptools

with open('./README.md', 'r', encoding='UTF-8') as readme_file:
    long_description = readme_file.read()

setuptools.setup(
    name='BangumiAPI',
    version='0.0.2',
    author='WhitePaper233',
    author_email='whitepaper.233@foxmail.com',
    description='番组计划开放API的Python模块',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/WhitePaper233/BangumiAPI',
    packages=setuptools.find_packages(),
    install_requires=['requests>=2.27.1'],
    python_requires='>=3.10',
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
