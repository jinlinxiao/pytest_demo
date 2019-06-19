# encoding: utf-8
"""
@author: jinlin.xiao
@file: test_parametrize.py
@time: 2019/6/3 9:57 AM
@desc:

pytest.mark.parametrize装饰器可以实现测试用例参数化

"""
import pytest


@pytest.mark.parametrize("test_input,expected",
                         [("3+5", 8),
                          ("2+4", 6),
                          ("6 * 9", 42),
                          ]
                         )
def test_eval(test_input, expected):
    assert eval(test_input) == expected



