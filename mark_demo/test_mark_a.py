# encoding: utf-8
"""
@author: jinlin.xiao
@file: test_mark_a.py
@time: 2019/5/28 11:56 AM
@desc:
"""
import pytest


class TestMark(object):
    ParamA = "param a"

    @pytest.mark.p0
    def test_mark_mass(self):
        x = "hello"
        assert x == "hello"

    @pytest.mark.manual
    def test_mark_manual(self):
        x = "hello"
        assert x == "hello"

    @pytest.mark.mass
    def test_mark_mass(self):
        x = "hello"
        assert x == "hello"

    @pytest.mark.p0
    @pytest.mark.manual
    def test_mark_manual_p0(self):
        x = "this"
        assert 'h' in x
        assert 'param' in self.ParamA

    @pytest.mark.p0
    @pytest.mark.mass
    def test_mark_mass_p0(self):
        x = "this"
        assert 'h' in x
        assert 'param' in self.ParamA

    @pytest.mark.manual
    @pytest.mark.mass
    def test_mark_mass_manual(self):
        x = "this"
        assert 'h' in x
        assert 'param' in self.ParamA


@pytest.mark.manual
def test_mark_manual():
    print("5")


@pytest.mark.mass
def test_mark_mass():
    assert 2 < 3


@pytest.mark.p0
def test_mark_p0():
    assert 2 < 3

