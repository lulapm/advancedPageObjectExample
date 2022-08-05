import pytest
from medium.pages.home_page import HomePage


@pytest.fixture(scope='module')
def home_page():
    return HomePage()

def test_register_newsletter_with_invalid_email(home_page):
    home_page.fill_newsletter_email_input('test.com')
    home_page.click_on_newsletter_submit_button()
    home_page.validate_invalid_newsletter_message(' Newsletter : Invalid email address.')


def test_register_newsletter_with_already_existent_email(home_page):
    home_page.fill_newsletter_email_input('test@test.com')
    home_page.click_on_newsletter_submit_button()
    home_page.validate_invalid_newsletter_message(' Newsletter : This email address is already registered.')
