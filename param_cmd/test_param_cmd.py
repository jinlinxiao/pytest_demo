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
        log.error("first")
    elif cmdopt == "type2":
        log.error("second")
    else:
        log.error("no cmdopt")


def test_env(env):
    if env == "live":
        log.error("live")
    elif env == "uat":
        log.error("uat")
    else:
        log.error("no env, env=%s" % env)


