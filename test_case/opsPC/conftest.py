import pytest
from apilist.login import login


@pytest.fixture(scope='session')
def login_start():
    """
    执行初始化登录操作，并返回token
    """
    return login()[1]

