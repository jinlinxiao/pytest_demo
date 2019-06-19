# encoding: utf-8
"""
@author: jinlin.xiao
@file: test_param_for_case.py
@time: 2019/6/3 10:41 AM
@desc:
标记单个测试实例在参数化
"""
import pytest


@pytest.mark.parametrize("in_param,expected",
                         [(5, 8),
                          (6, 9),
                          (12, 15),
                          pytest.param(1, 5, marks=pytest.mark.xfail),
                          ])
def test_add_3(in_param, expected):
    """测试add 3之后的值"""
    assert in_param + 3 == expected
