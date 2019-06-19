# encoding: utf-8
"""
@author: jinlin.xiao
@file: test_func_class.py
@time: 2019/6/2 8:19 AM
@desc:
"""
import pytest


# setup和teardown有同样的效果
def setup():
    print("func_setup：每个用例开始前都会执行")


def teardown():
    print("func_teardown：每个用例结束后都会执行")


def setup_function():
    print("func_setup_function：每个用例开始前都会执行")


def teardown_function():
    print("func_teardown_function：每个用例结束后都会执行")


def test_one():
    print("正在执行----func_test_one")
    x = "this"
    assert 'h' in x


def test_two():
    print("正在执行----func_test_two")
    assert True


def test_three():
    print("正在执行----func_test_three")
    a = "hello"
    b = "hello world"
    assert a in b


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
    pytest.main(["-v", "test_func_class.py"])

