# encoding: utf-8
"""
@author: jinlin.xiao
@file: test_dep_by_casename.py
@time: 2022/11/23 14:27
@desc:

@pytest.mark.dependency(name=None,depends=[],scope=‘module’)的括号中参数说明如下：

name：依赖测试所引用的测试名称，如果未设置，则默认使用pytest定义的节点ID，名称需唯一
depends：依赖性，此测试所依赖的测试名称的列表
scope：搜索依赖的范围，必须是session,package,module或class,默认为module

————————————————
版权声明：本文为CSDN博主「永远不要矫情」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/dingding_ting/article/details/117200319

"""
import pytest


@pytest.mark.dependency()
def test_1_1():
    print("hello test_1_1")
    assert 1 == 1


@pytest.mark.dependency()
def test_1_2():
    print("hello test_1_2")
    assert 2 == 1


@pytest.mark.dependency(depends=['test_1_1'])
def test_2_1():
    print("hello test_2_1")


@pytest.mark.dependency(depends=['test_1_2'])
def test_2_2():
    print("hello test_2_2")
# test_dep_by_casename.py::test_2_2 SKIPPED (test_2_2 depends on test_1_2) [ 80%]
# Skipped: test_2_2 depends on test_1_2


@pytest.mark.dependency(depends=['dep'])
def test_2_3():
    print("hello test_2_3")
# test_dep_by_casename.py::test_2_3 SKIPPED (test_2_3 depends on test_3_2) [ 71%]
# Skipped: test_2_3 depends on test_3_2


@pytest.mark.dependency()
def test_3_1():
    print("hello test_3_1")


@pytest.mark.dependency(name='dep')
def test_3_2():
    print("hello test_3_2")
    assert 2 == 1


if __name__ == '__main__':
    pytest.main(['-sv'])

