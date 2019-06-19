# encoding: utf-8
"""
@author: jinlin.xiao
@file: test_pytest_log.py
@time: 2019/6/10 9:27 AM
@desc:
在 pytest.ini 中，增加相关配置
如果需要在命令行中重新定义，使用 -o 选项
"""
import logging
log = logging.getLogger(__name__)


def test_func_a():
    log.debug("test_func_a debug log.")
    log.info("test_func_a info log.")
    log.warning("test_func_a. warning log.")
    log.error("test_func_a. error log.")


def test_func_b():
    log.debug("test_func_b debug log.")
    log.info("test_func_b info log.")
    log.warning("test_func_b. warning log.")
    log.error("test_func_b. error log.")
    assert 1 == 2


def test_func_c():
    log.debug("test_func_c debug log.")
    log.info("test_func_c info log.")
    log.warning("test_func_c. warning log.")
    log.error("test_func_c. error log.")

