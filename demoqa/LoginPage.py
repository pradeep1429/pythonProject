from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

class LoginPage:


    LOGIN_BUTTON = (By.ID,"login")
    USER_INPUT = (By.ID,"userName")
    PASSWORD_INPUT = (By.ID,"password")
    LOGGED_IN_USER = (By.XPATH, "//label[@id='userName-value']")
    LOGOUT_LINK = (By.ID, "submit")


    def __init__(self, driver,logger):
        self.driver = driver
        self.log = logger

    def open_login_page(self):
        self.driver.find_element(*LoginPage.LOGIN_BUTTON).click()
        self.log.info("Login page opened")

    def login(self, userName, password):
        self.driver.find_element(*LoginPage.USER_INPUT).send_keys(userName)
        self.log.info(f"Entered Username: {userName}")
        self.driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(password)
        self.log.info(f"Entered Password: {password}")
        self.driver.find_element(*LoginPage.LOGIN_BUTTON).click()
        try:
            element = self.driver.find_element(By.XPATH, "//*[@id='my-id-1']")
            assert userName in self.driver.find_element(*LoginPage.LOGGED_IN_USER).text
            self.log.info("Login Success")
        except NoSuchElementException:
            self.log.error("Login is not successful")
            assert False


    def logout(self):
        self.driver.find_element(*LoginPage.LOGOUT_LINK).click()
        self.log.info("Logout Success")

