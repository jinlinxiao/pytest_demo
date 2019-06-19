# encoding: utf-8
"""
@author: jinlin.xiao
@file: test_fix1.py
@time: 2019/6/2 8:53 AM
@desc:
"""
import pytest


def test_s1(login):
    print("用例1：登录之后其它动作111")


def test_s2():  # 不传login
    print("用例2：不需要登录，操作222")


def test_s3(login):
    print("用例3：登录之后其它动作333")


if __name__ == "__main__":
    pytest.main(["-s", "test_fix1.py"])
