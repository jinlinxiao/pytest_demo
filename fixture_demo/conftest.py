# encoding: utf-8
"""
@author: jinlin.xiao
@file: conftest.py
@time: 2019/6/2 8:52 AM
@desc:
"""

import pytest


@pytest.fixture()
def login():
    print("输入账号，密码先登录")


@pytest.fixture(scope="module")
def open():
    print("打开浏览器，并且打开百度首页")


@pytest.fixture(scope="module")
def open_with_exit():
    print("打开浏览器，并且打开百度首页")
    yield
    print("执行teardown")
    print("关闭浏览器")
