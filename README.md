# PyBangumi

[![codecov](https://codecov.io/gh/DaydreamCafe/PyBangumi/branch/Dev/graph/badge.svg?token=R69F2D4K2I)](https://codecov.io/gh/DaydreamCafe/PyBangumi)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

番组计划 ( https://bangumi.tv/ ) 开放API的Python模块

## Usage

```python
import pybangumi as pybgm


api = pybgm.BangumiAPI()
print(api.new_user('233').fetch())
```