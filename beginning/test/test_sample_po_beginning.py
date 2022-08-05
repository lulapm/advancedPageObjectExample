from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from hamcrest import assert_that, is_


def test_register_newsletter_with_invalid_email():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('http://automationpractice.com/')
    driver.find_element(By.CSS_SELECTOR, '#newsletter-input').send_keys('test.com')
    driver.find_element(By.CSS_SELECTOR, '#submitNewsletter').click()
    message = driver.find_element(By.CSS_SELECTOR, '.alert-danger').text
    assert_that(message, is_(' Newsletter : Invalid email address.'))


def test_register_newsletter_with_already_existent_email():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('http://automationpractice.com/')
    driver.find_element(By.CSS_SELECTOR, '#newsletter-input').send_keys('test@test.com')
    driver.find_element(By.CSS_SELECTOR, '#submitNewsletter').click()
    message = driver.find_element(By.CSS_SELECTOR, '.alert-danger').text
    assert_that(message, is_(' Newsletter : This email address is already registered.'))
