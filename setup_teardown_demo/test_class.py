# encoding: utf-8
"""
@author: jinlin.xiao
@file: test_function.py
@time: 2019/6/2 7:46 AM
@desc:
"""
import pytest


# setup和teardown有同样的效果
def setup():
    print("setup：每个用例开始前都会执行")


def teardown():
    print("teardown：每个用例结束后都会执行")


def setup_module():
    print("setup_module：整个.py模块只执行一次,比如：所有用例开始前只打开一次浏览器")


def teardown_module():
    print("teardown_module：整个.py模块只执行一次,比如：所有用例结束后再关闭浏览器")


def setup_function():
    print("setup_function：每个用例开始前都会执行")


def teardown_function():
    print("teardown_function：每个用例结束后都会执行")


class TestCase(object):

    def setup(self):
        print("class_setup: 每个用例开始前执行")

    def teardown(self):
        print("class_teardown: 每个用例结束后执行")

    def setup_class(self):
        print("class_setup_class：所有用例执行之前")

    def teardown_class(self):
        print("class_teardown_class：所有用例执行之前")

    def setup_method(self):
        print("class_setup_method:  每个用例开始前执行")

    def teardown_method(self):
        print("class_teardown_method:  每个用例结束后执行")

    def test_one(self):
        print("正在执行----test_class_one")
        x = "this"
        assert 'h' in x

    def test_two(self):
        print("正在执行----test_class_two")
        assert True

    def test_three(self):
        print("正在执行----test_class_three")
        a = "hello"
        b = "hello world"
        assert a in b


if __name__ == "__main__":
    pytest.main(["-v", "test_class.py"])

