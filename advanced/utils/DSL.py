from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class DSL:


    def __init__(self, driver):
        self.driver = driver
    
    
    def visit(self, url):
        self.driver.get(url)


    def click(self, locator, seconds=20):
        self.wait_for(EC.element_to_be_clickable(locator), seconds).click()
    
    
    def find_element(self, locator, seconds=20):
        element = self.wait_for(EC.visibility_of_element_located(locator), seconds)
        return element


    def find_element_by_presence(self, locator, seconds=20):
        element = self.wait_for(EC.presence_of_element_located(locator), seconds)
        return element


    def wait_for(self,condition, seconds = 20):
        return  WebDriverWait(self.driver, seconds).until(condition)
    
    
    def type_in(self, locator, text, set_clear=True, seconds=20):
        element = self.find_element(locator, seconds)
        if set_clear:
            element.clear()
        element.send_keys(text)


    def pause(self, time):
        ActionChains(self.driver).pause(time).perform()


    def execute_js(self, script):
        self.driver.execute_script(script)


    def move_to_element(self, locator, seconds=10):
        element = self.find_element_by_presence(locator, seconds)
        ActionChains(self.driver).move_to_element(element).perform()
