from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from hamcrest import assert_that, is_

class HomePage():

    # Locators
    newsletter_email_input = (By.CSS_SELECTOR, '#newsletter-input')
    newsletter_submit_button = (By.NAME, '#submitNewsletter')
    validation_message = (By.CSS_SELECTOR, '.alert-danger')


    def get_driver():
        return webdriver.Chrome(ChromeDriverManager().install())


    # Actions
    def fill_newsletter_email_input(self, email):
        driver = self.get_driver()
        driver.find_element(By.CSS_SELECTOR, self.newsletter_email_input).send_keys(email)

    
    def click_on_newsletter_submit_button(self):
        driver = self.get_driver()
        driver.find_element(By.CSS_SELECTOR, self.newsletter_submit_button).click()


    # Assertions
    def validate_invalid_newsletter_message(self, message):
        driver = self.get_driver()
        message_of_element = driver.find_element(By.CSS_SELECTOR, self.validation_message).text
        assert_that(message_of_element, is_(message))
