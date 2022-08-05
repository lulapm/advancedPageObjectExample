import os
import sys

PARENT_PATH = os.path.abspath("..")
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)

from advanced.pages.home.home_map import HomeMap
from advanced.utils.DSL import DSL
from selenium.webdriver.common.by import By

class HomePage():


    def __init__(self, driver):
        self.driver = driver
        self.locators = HomeMap()


    def fill_newsletter_email_input(self, email):
        DSL(self.driver).move_to_element(self.locators.newsletter_email_input)
        DSL(self.driver).pause(2)
        DSL(self.driver).type_in(self.locators.newsletter_email_input, email)

    
    def click_on_newsletter_submit_button(self):
        DSL(self.driver).click(self.locators.newsletter_submit_button)

    
    def register_newsletter(self, email):
        self.fill_newsletter_email_input(email)
        self.click_on_newsletter_submit_button()
