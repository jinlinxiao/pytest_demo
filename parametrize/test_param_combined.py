# encoding: utf-8
"""
@author: jinlin.xiao
@file: test_param_combined.py
@time: 2019/6/3 10:50 AM
@desc:
堆叠参数化装饰器，得到多个参数化参数的所有组合
"""

import pytest


@pytest.mark.parametrize("x", [0, 1], ids=["name0", "name1"])
@pytest.mark.parametrize("y", [2, 3], ids=["name2", "name3"])
def test_foo(x, y):
    print("测试数据组合：x->%s, y->%s" % (x, y))


if __name__ == "__main__":
    pytest.main(["-s", "test_param_combined.py"])
