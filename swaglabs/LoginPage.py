
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

class LoginPage:

    USER_INPUT = (By.ID,"user-name")
    PASSWORD_INPUT = (By.ID,"password")
    PRODUCTS_TITLE = (By.XPATH, "//div[@class='header_secondary_container']/span")
    LOGIN_BUTTON = (By.ID, "login-button")
    LEFT_MENU = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    ERROR_MSG = (By.XPATH, "//h3[@data-test='error']")

    ERROR_MESSAGE = "Epic sadface: Sorry, this user has been locked out."


    def __init__(self, driver,logger):
        self.driver = driver
        self.log = logger

    def open_login_page(self):
        if not self.driver.current_url == "https://www.saucedemo.com/":
            self.driver.get("https://www.saucedemo.com/")
    def login(self, userName, password):
        self.open_login_page()
        self.driver.find_element(*LoginPage.USER_INPUT).clear()
        self.driver.find_element(*LoginPage.USER_INPUT).send_keys(userName)
        self.log.info(f"Entered Username: {userName}")
        self.driver.find_element(*LoginPage.PASSWORD_INPUT).clear()
        self.driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(password)
        self.log.info(f"Entered Password: {password}")
        self.driver.find_element(*LoginPage.LOGIN_BUTTON).click()

    def successful_login(self,userName, password):
        self.login(userName, password)
        try:
            assert "Products" in self.driver.find_element(*LoginPage.PRODUCTS_TITLE).text
            self.log.info("Login Success")
        except NoSuchElementException:
            self.log.error("Login is not successful")
            assert False

    def locked_user(self, userName, password):
        self.login(userName, password)
        try:
            assert self.ERROR_MESSAGE in self.driver.find_element(*LoginPage.ERROR_MSG).text
            self.log.info(f"Given user is locked. info: {self.ERROR_MESSAGE}")
        except NoSuchElementException:
            self.log.error("Login is not successful")
            assert False



    def logout(self):
        self.driver.find_element(*LoginPage.LEFT_MENU).click()
        self.driver.find_element(*LoginPage.LOGOUT_LINK).click()
        self.log.info("Logout Success")

