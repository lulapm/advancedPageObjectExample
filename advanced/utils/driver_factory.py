import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class DriverFactory():


    def __init__(self):
        self.driver = None


    def instance_driver(self):
        if self.driver is None:
            self.driver = self.factory()
        return self.driver 


    def factory(driver_param):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.set_page_load_timeout(1000)
        return driver
