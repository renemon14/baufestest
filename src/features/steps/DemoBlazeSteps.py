import os
import random
import time
from assertpy import assert_that
from behave import *
from elements import DemoBlazePage
from functions.GeneralFunctions import General_Functions

functions = General_Functions()

GLOBAL = {}

@step('site to navigate: "{url}"')
def step_impl(self, url):
    self.driver.get(os.getenv(url))


@step('register with user: "{}" and pass: "{}"')
def step_impl(self, user, passw):
    GLOBAL['USERNAME'] = user + str(random.randrange(1, 9999))
    GLOBAL['PASSWORD'] = passw
    functions.click_element(DemoBlazePage.MENU_SIGNUP)
    functions.send_key(DemoBlazePage.INPUT_USER, GLOBAL['USERNAME'])
    functions.send_key(DemoBlazePage.INPUT_PASS, GLOBAL['PASSWORD'])
    functions.click_element(DemoBlazePage.BTN_REGISTER)
    time.sleep(2)
    alert = self.driver.switch_to.alert
    alert.accept()

@step('login user')
def step_impl(self):
    functions.click_element(DemoBlazePage.MENU_LOGIN)
    functions.send_key(DemoBlazePage.LOGIN_USER, GLOBAL['USERNAME'])
    functions.send_key(DemoBlazePage.LOGIN_PASS, GLOBAL['PASSWORD'])
    functions.click_element(DemoBlazePage.BTN_LOGIN)
    functions.implicit_wait_visible(DemoBlazePage.MENU_LOGOUT)
    UserText = self.driver.find_element(*DemoBlazePage.NAME_USER).text
    assert GLOBAL['USERNAME'] in UserText


@step('logout user')
def step_impl(self):
    functions.click_element(DemoBlazePage.MENU_LOGOUT)
    functions.implicit_wait_visible(DemoBlazePage.MENU_LOGIN)


@step('add laptop to cart')
def step_impl(self):
    functions.click_element(DemoBlazePage.CATEG_LAPTOPS)
    time.sleep(2)
    LaptopText = self.driver.find_element(*DemoBlazePage.FIRST_CONTENT_LAPTOP).text
    assert "laptop" in LaptopText
    functions.click_element(DemoBlazePage.FIRST_LAPTOP)
    functions.click_element(DemoBlazePage.ADD_CART)
    time.sleep(2)
    alert = self.driver.switch_to.alert
    alert.accept()


@step('validate product in cart')
def step_impl(self):
    functions.click_element(DemoBlazePage.MENU_CART)
    functions.implicit_wait_visible(DemoBlazePage.PRODUCT_CART)



