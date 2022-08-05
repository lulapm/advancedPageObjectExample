from selenium.webdriver.common.by import By

class HomeMap():

    newsletter_email_input = (By.CSS_SELECTOR, '#newsletter-input')
    newsletter_submit_button = (By.NAME, '#submitNewsletter')
    validation_message = (By.CSS_SELECTOR, '.alert-danger')
