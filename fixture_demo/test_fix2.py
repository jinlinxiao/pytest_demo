# encoding: utf-8
"""
@author: jinlin.xiao
@file: test_fix2.py
@time: 2019/6/2 8:54 AM
@desc:
"""
import pytest


def test_s4(login):
    print("用例4：登录之后其它动作111")


def test_s5():  # 不传login
    print("用例5：不需要登录，操作222")


if __name__ == "__main__":
    pytest.main(["-s", "test_fix2.py"])
