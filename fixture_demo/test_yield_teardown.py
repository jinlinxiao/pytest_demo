# encoding: utf-8
"""
@author: jinlin.xiao
@file: test_yield_teardown.py
@time: 2019/6/2 9:05 AM
@desc:
"""


def test_fix2_s1():
    print("用例yield_1：搜索python-1")


def test_fix2_s2(open_with_exit):
    print("用例yield_2：搜索python-2")


def test_fix2_s3():
    print("用例yield_3：搜索python-3")

