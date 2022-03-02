# encoding: utf-8
"""
@author: jinlin.xiao
@file: test_param_1.py
@time: 2021/3/15 4:56 PM
@desc:
"""
import pytest
import logging
log = logging.getLogger(__name__)


data_1 = [
    pytest.param(1, 2, 3, id="(a+b):pass"),  # id的值可以自定义， 只要方便理解每个用例是干什么的即可
    pytest.param(4, 5, 9, id="(a+b):fail")
]


# def fix_1(cmdopt):
#     print('\n --cmdopt的值：',cmdopt)

# TestParametrizeData = None
#
#
# @pytest.fixture(autouse=True)
# def setup(cmdopt):
#     global TestParametrizeData
#     if cmdopt == "type1":
#         log.error("first222222")
#         TestParametrizeData = [
#             pytest.param(1, 2, 3, id="(a+b):pass first"),  # id的值可以自定义， 只要方便理解每个用例是干什么的即可
#             pytest.param(4, 5, 9, id="(a+b):fail first")
#         ]
#     elif cmdopt == "type2":
#         log.error("second2222222")
#         TestParametrizeData = [
#             pytest.param(1, 2, 3, id="(a+b):pass second"),  # id的值可以自定义， 只要方便理解每个用例是干什么的即可
#             pytest.param(4, 5, 9, id="(a+b):fail second")
#         ]
#     else:
#         log.error("no cmdopt")
#         TestParametrizeData = data_1
#     # return data_1


def add(a, b):
    return a + b


# class TestParametrize(object):
#
#     # @pytest.fixture(autouse=True)
#     # def get_data(self, request):
#     #     cmdopt=request.config.getoption("--cmdopt")
#     #     if cmdopt == "type1":
#     #         TestParametrizeData = [
#     #             pytest.param(1, 2, 3, id="(a+b):pass")
#     #         ]
#     #     yield
#         # db.rollback()
#
#     # def setup(self):
#     #     if cmdopt == "type1":
#     #         log.error("first222222")
#     #     elif cmdopt == "type2":
#     #         log.error("second2222222")
#     #     else:
#     #         log.error("no cmdopt")
#
#     @pytest.mark.parametrize('a, b, expect', data_1)
#     def test_parametrize_1(self, a, b, expect):
#         assert add(a, b) == expect


# @pytest.mark.parametrize('a, b, expect', data_1)
# def test_parametrize_1(a, b, expect):
#     assert add(a, b) == expect


# def test_settle_data(settle_data):
#     log.error(settle_data)
    # a, b, expect = settle_data
    # assert add(a, b) == expect


class TestSettleData(object):

    def setup(self):
        log.error("setup")
        # self.settle_data = settle_data
        # log.error(type(self.settle_data))

    def test_1(self, settle_data):
        self.settle_data = settle_data
        log.error(self.settle_data)

    def teardown(self):
        log.error("teardown")


# def test_settle_data_a_b(settle_datas, a, b):
#     log.error(settle_datas, a, b)

# def test_compute(param1):
#     assert param1 < 4


if __name__ == '__main__':
    pytest.main(['-v'])
