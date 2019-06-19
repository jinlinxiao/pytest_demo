# encoding: utf-8
"""
@author: jinlin.xiao
@file: conftest.py
@time: 2019/6/14 9:46 AM
@desc:
"""
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="type1", help="my option: type1 or type2"
    )
    parser.addoption(
        "--env", action="store", default="test", help="run env: test or uat or live"
    )


@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")


@pytest.fixture
def env(request):
    return request.config.getoption("--env")

