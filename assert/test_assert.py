# encoding: utf-8
"""
@author: jinlin.xiao
@file: test_assert.py
@time: 2019/6/4 8:55 AM
@desc:

在异常的时候，输出一些提示信息
assert a % 2 == 0, "判断a为偶数，当前a的值为：%s"%a

引发异常的断言

"""
import pytest


def test_assert_no_msg():
    a = 3
    assert a % 2 == 0


def test_assert_with_msg():
    a = 3
    assert a % 2 == 0, "判断a为偶数，当前a的值为：%s" % a
