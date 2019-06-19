# encoding: utf-8
"""
@author: jinlin.xiao
@file: test_assert_raise.py
@time: 2019/6/4 9:04 AM
@desc:
"""
import pytest


def test_zero_division_no_catch():
    """断言异常"""
    print(1 / 0)


def test_zero_division():
    """断言异常"""
    with pytest.raises(ZeroDivisionError) as exc_info:
        print(1 / 0)

    # 断言异常类型type
    assert exc_info.type == ZeroDivisionError
    # 断言异常value值
    assert "division by zero" in str(exc_info.value)

