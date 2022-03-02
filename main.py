# encoding: utf-8
"""
@author: jinlin.xiao
@file: main.py
@time: 2021/3/15 4:14 PM
@desc:
"""
import pytest


if __name__ == '__main__':
    # pytest.main(["-x", "param1"])
    # pytest.main(["--cmdopt", "type1", "--env", "uat", "-x", "param1"])
    # pytest.main(["--cmdopt", "type1", "--env", "uat", "-x", "param1", "param2"])
    # pytest.main(["--cmdopt", "type1", "--env", "uat", "-s", "param1/test_param_cmd12.py", "param2/test_param_cmd22.py"])
    # pytest.main(["--cmdopt", "type1", "--env", "uat", "-x", "param1/test_param_cmd12.py", "param2/test_param_cmd22.py"])
    # pytest.main(["--cmdopt", "type1", "--env", "uat", "--html", "report.html", "--self-contained-html", "-x", "param1/test_param_cmd12.py", "param2/test_param_cmd22.py"])

    # 参数化验证
    pytest.main(["--cmdopt", "type1", "--env", "uat", "-s", "parametrize/test_param_1.py"])
    # pytest.main(["--cmdopt", "type2", "--env", "uat", "-s", "parametrize/test_param_1.py"])

