import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", action="store")
    parser.addoption("--branch", action="store")

"""
@pytest.fixture(scope='session')
def name(request):
    name_value = request.config.option.name
    if name_value is None:
        pytest.skip()
    return name_value
"""