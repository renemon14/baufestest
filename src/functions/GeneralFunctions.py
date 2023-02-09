import logging

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class General_Functions:

    driver = None
    timeWait = 30

    def implicit_wait_visible(self, locator):
        try:
            wait = WebDriverWait(self.driver, self.timeWait)
            wait.until(EC.visibility_of_element_located(locator))
            logging.info("[INFO]: Element Visible")

        except TimeoutException:
            raise ValueError("[ERROR]: Element NO visible")

    def implicit_wait_present(self, locator):
        try:
            wait = WebDriverWait(self.driver, self.timeWait)
            wait.until(EC.presence_of_element_located(locator))
            logging.info("[INFO]: Element present")

        except TimeoutException:
            raise ValueError("[ERROR]: Element NO present")

    def implicit_wait_clickable(self, locator):
        try:
            wait = WebDriverWait(self.driver, self.timeWait)
            wait.until(EC.element_to_be_clickable(locator))
            logging.info("[INFO]: Element clickable")

        except TimeoutException:
            raise ValueError("[ERROR]: Element NO clickable")

    def click_element(self, locator):
        try:
            General_Functions.implicit_wait_clickable(self, locator)
            self.driver.find_element(*locator).click()

        except:
            raise ValueError("[ERROR]: Element NO clickable")


    def send_key(self, locator, text):
        try:
            General_Functions.implicit_wait_visible(self, locator)
            element = self.driver.find_element(*locator)
            length =len(element.get_attribute('value'))
            element.send_keys(length * Keys.BACKSPACE)
            element.send_keys(text)
        except:
            raise ValueError("[ERROR]: No such element")

    def move_to_element(self, locator1, locator2):
        General_Functions.implicit_wait_present(self, locator1)
        General_Functions.implicit_wait_present(self, locator2)
        menu_element = self.driver.find_element(*locator1)
        submenu_element = self.driver.find_element(*locator2)
        build = ActionChains(self.driver)
        build.move_to_element(menu_element).click(submenu_element).perform()