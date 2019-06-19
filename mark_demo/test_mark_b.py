# encoding: utf-8
"""
@author: jinlin.xiao
@file: test_mark_b.py
@time: 2019/5/28 11:56 AM
@desc:
"""
import pytest


class TestMarkB(object):
    ParamA = "param a"

    @pytest.mark.manual
    def test_mark_manual(self):
        x = "this"
        assert 'h' in x
        assert 'param' in self.ParamA

    @pytest.mark.p0
    @pytest.mark.mass
    def test_mark_mass_p0(self):
        x = "hello"
        assert x == "hello"

    @pytest.mark.skip
    def test_mark_skip(self):
        assert 2 < 3


@pytest.mark.manual
def test_mark_manual():
    print("5")


@pytest.mark.mass
def test_mark_mass():
    assert 2 < 3


@pytest.mark.mass
@pytest.mark.skip
def test_mark_mass_skip():
    assert 2 < 3


