# encoding: utf-8
"""
@author: jinlin.xiao
@file: test_function.py
@time: 2019/6/2 7:46 AM
@desc:
"""
import pytest


def setup_module():
    print("setup_module：整个.py模块只执行一次,比如：所有用例开始前只打开一次浏览器")


def teardown_module():
    print("teardown_module：整个.py模块只执行一次,比如：所有用例结束后再关闭浏览器")


def setup_function():
    print("setup_function：每个用例开始前都会执行")


def teardown_function():
    print("teardown_function：每个用例结束后都会执行")


# setup和teardown跟setup_function和teardown_function有同样的效果，一般二者选其一即可
def setup():
    print("setup：每个用例开始前都会执行")


def teardown():
    print("teardown：每个用例结束后都会执行")


def test_one():
    print("正在执行----test_one")
    x = "this"
    assert 'h' in x


def test_two():
    print("正在执行----test_two")
    assert True


def test_three():
    print("正在执行----test_three")
    a = "hello"
    b = "hello world"
    assert a in b


if __name__ == "__main__":
    pytest.main(["-v", "test_function.py"])

