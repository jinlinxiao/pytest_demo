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


@pytest.fixture(scope="session")
def cmdopt(request):
    return request.config.getoption("--cmdopt")


@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")


def pytest_generate_tests(metafunc):
    print("pytest_generate_tests")
    if "settle_data" in metafunc.fixturenames:
        if metafunc.config.getoption("--cmdopt") == "type1":
            SeData = [
                pytest.param("1", id="(a+b):pass---conf-type1"),
                pytest.param("1,2", id="(a+b):pass---conf-type1"),
                pytest.param("1,2,3", id="(a+b):pass---conf-type1")
            ]
        else:
            SeData = [
                pytest.param("1", id="(a+b):pass---conf")
            ]
        metafunc.parametrize("settle_data", SeData)
    # if "settle_datas" in metafunc.fixturenames:
    #     if metafunc.config.getoption("--cmdopt") == "type1":
    #         SeData = [
    #             pytest.param(1,2,3, id="(a+b):pass---conf-type1")
    #         ]
    #     else:
    #         SeData = [
    #             pytest.param(1,2,3, id="(a+b):pass---conf")
    #         ]
    #     metafunc.parametrize("settle_datas,a,b", SeData)

