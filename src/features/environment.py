from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import logging, os
from dotenv import load_dotenv
from functions.GeneralFunctions import General_Functions

### HOOKS ###

### Before Tests ###


def before_all(self):

    load_dotenv()
    self.variablesTemp = {}
    self.http_request_header = {}
    self.http_request_body = {}
    self.responseParse = ''

def before_feature(self, feature):

    if "Test" in feature.tags:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                       chrome_options=chrome_options)
        General_Functions.driver = self.driver



### After Tests ###

def after_feature(self, feature):
    if "Test" in feature.tags:
        self.driver.quit()