# encoding: utf-8
"""
@author: jinlin.xiao
@file: test_sample_class.py
@time: 2019/5/23 7:50 PM
@desc:
pytest的一个示例,测试类
"""


class TestClass:
    ParamA = "param a"

    def test_one(self):
        x = "this"
        assert 'h' in x
        assert 'param' in self.ParamA

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')

