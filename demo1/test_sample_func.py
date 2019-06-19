# encoding: utf-8
"""
@author: jinlin.xiao
@file: test_sample_func.py.py
@time: 2019/5/23 7:36 PM
@desc:
pytest的一个示例,测试函数
"""


def func(x):
    return x + 1


def test_answer_fail():
    assert func(3) == 5


def test_answer_suc():
    assert func(3) == 4


def test_no_assert():
    print("5")

