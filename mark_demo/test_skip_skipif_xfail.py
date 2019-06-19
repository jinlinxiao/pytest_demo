# encoding: utf-8
"""
@author: jinlin.xiao
@file: test_skip_skipif_xfail.py
@time: 2019/5/31 4:02 PM
@desc:
"""
import pytest
RunType = 'uat'


class TestSkipClass(object):
    ParamA = "param a"

    @pytest.mark.skip(reason="skip mark test")
    def test_mark_skip(self):
        x = "this"
        assert 'h' in x
        assert 'param' in self.ParamA

    def test_skip_in_run(self):
        if True:
            pytest.skip("skip in running case.")
        assert True

    @pytest.mark.xfail
    def test_mark_mass_xfail(self):
        x = "hello"
        assert x == "hello_error"

    @pytest.mark.xfail
    def test_mark_mass_xfail_suc(self):
        x = "hello"
        assert x == "hello"

    @pytest.mark.skipif(RunType == "test", reason="skip in test env")
    def test_mark_skip_if(self):
        assert 2 < 3


@pytest.mark.skipif(RunType == "uat", reason="skip in uat env")
class TestSkipUAT(object):
    ParamA = "param a"

    def test_mark_skip_if_uat_a(self):
        x = "this"
        assert 'h' in x
        assert 'param' in self.ParamA

    def test_mark_skip_if_uat_b(self):
        x = "this"
        assert 'h' in x
        assert 'param' in self.ParamA


@pytest.mark.manual
def test_mark_manual():
    print("5")

