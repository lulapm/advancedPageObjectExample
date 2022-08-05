import os
import sys
import pytest

PARENT_PATH = os.path.abspath("..")
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)

from advanced.utils.constants import Constants
from advanced.utils.data_tests import DataTests
from advanced.utils.driver_factory import DriverFactory
from advanced.pages.home.home_page import HomePage
from advanced.pages.home.home_validator import HomeValidator


@pytest.fixture(scope='module')
def home_page():
    return HomePage(DriverFactory().instance_driver())


@pytest.fixture(scope='module')
def home_validator():
    return HomeValidator(DriverFactory().instance_driver())


def test_register_newsletter_with_invalid_email(home_page, home_validator):
    home_page.register_newsletter(DataTests().invalid_email)
    home_validator.validate_invalid_newsletter_message(Constants().invalid_newsletter_email_message)


def test_register_newsletter_with_already_existent_email(home_page, home_validator):
    home_page.register_newsletter(DataTests().already_existent_email)
    home_validator.validate_invalid_newsletter_message(Constants().already_existent_email)
