# encoding: utf-8
"""
@author: jinlin.xiao
@file: test_param_cmd.py
@time: 2019/6/14 9:48 AM
@desc:

命令行传参数

"""
import pytest
import logging
log = logging.getLogger(__name__)


def test_cmdopt(cmdopt):
    if cmdopt == "type1":
        log.error("first 22")
    elif cmdopt == "type2":
        log.error("second 22")
    else:
        log.error("no cmdopt 22")


def test_env(env):
    if env == "live":
        log.error("live  22")
    elif env == "uat":
        log.error("uat  22")
    else:
        log.error("no env  22, env=%s" % env)


