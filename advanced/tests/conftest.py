import os
import sys
import pytest

PARENT_PATH = os.path.abspath("..")
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)

from advanced.utils.DSL import DSL
from advanced.utils.constants import Constants
from advanced.utils.driver_factory import DriverFactory


@pytest.fixture(autouse=True, scope='session')
def setup_teardown():
    driver = DriverFactory().instance_driver()
    DSL(driver).visit(Constants.url)
    yield
    driver.quit()


# def pytest_addoption(parser):
#     parser.addoption("--driver", action="store")


# @pytest.fixture(scope='session')
# def driver_param(request):
#     print('aqui')
#     driver_param_value = request.config.option.driver
#     if driver_param_value is None:
#         pytest.skip()
#     return driver_param_value
