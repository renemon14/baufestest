from selenium.webdriver.common.by import By

MENU_SIGNUP = (By.CSS_SELECTOR, "li > a#signin2")
MENU_LOGIN = (By.CSS_SELECTOR, "li > a#login2")
MENU_LOGOUT = (By.CSS_SELECTOR, "li > a[onclick='logOut()']")
MENU_CART = (By.CSS_SELECTOR, "li > a#cartur")

INPUT_USER = (By.CSS_SELECTOR, "input#sign-username")
INPUT_PASS = (By.CSS_SELECTOR, "input#sign-password")
BTN_REGISTER = (By.CSS_SELECTOR, "button[onclick='register()']")

LOGIN_USER = (By.CSS_SELECTOR, "input#loginusername")
LOGIN_PASS = (By.CSS_SELECTOR, "input#loginpassword")
BTN_LOGIN = (By.CSS_SELECTOR, "button[onclick='logIn()']")

NAME_USER = (By.CSS_SELECTOR, "li > a#nameofuser")

CATEG_LAPTOPS = (By.CSS_SELECTOR, "div > a[onclick=\"byCat('notebook')\"]")
FIRST_CONTENT_LAPTOP = (By.CSS_SELECTOR, "#tbodyid > div:nth-child(1) > div")
FIRST_LAPTOP = (By.CSS_SELECTOR, "#tbodyid > div:nth-child(1) > div > a")

ADD_CART = (By.CSS_SELECTOR, "div > a[onclick='addToCart(8)']")
PRODUCT_CART = (By.CSS_SELECTOR, "#tbodyid > tr")
