# PyBangumi

[![codecov](https://codecov.io/gh/DaydreamCafe/PyBangumi/branch/Dev/graph/badge.svg?token=R69F2D4K2I)](https://codecov.io/gh/DaydreamCafe/PyBangumi)

番组计划 ( https://bangumi.tv/ ) 开放API的Python模块

## Usage

```python
import pybangumi as pybgm


api = pybgm.BangumiAPI('Me/MyProject (https://github.com/Me/MyProject)')
print(api.new_user('233').fetch())
```