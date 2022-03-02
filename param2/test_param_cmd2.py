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
        log.error("first222222")
    elif cmdopt == "type2":
        log.error("second2222222")
    else:
        log.error("no cmdopt")


def test_env(env):
    if env == "live":
        log.error("live 22222")
    elif env == "uat":
        log.error("uat 22222")
    else:
        log.error("no env 22222, env=%s" % env)


