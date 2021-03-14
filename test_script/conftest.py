# content of conftest.py
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--key", action="store", default=None, help="单独用例执行名称"
    )


@pytest.fixture
def key(request):
    return request.config.getoption("--key")
