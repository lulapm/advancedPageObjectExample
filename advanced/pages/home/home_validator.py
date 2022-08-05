import os
import sys
from hamcrest import assert_that, is_

PARENT_PATH = os.path.abspath("..")
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)

from advanced.pages.home.home_map import HomeMap
from advanced.utils.DSL import DSL

class HomeValidator():


    def __init__(self, driver):
        self.DSL = DSL(driver)
    

    def validate_invalid_newsletter_message(self, message):
        element = self.DSL.find_element(HomeMap.validation_message)
        assert_that(element.text, is_(message))
