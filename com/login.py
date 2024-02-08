import time

import pytest

from swaglabs.LoginPage import LoginPage
from utility.Base import Base

@pytest.mark.usefixtures("setup")
class TestLogin():
    log = Base.getLogger()
    # def test_get_session(self,setup_session):
    #     self.driver = setup_session
    #     return self.driver

    def test_login_swaglabs(self):
        loginPage = LoginPage(self.driver,self.log)
        self.log.info(f"self driver ref is:{id(self.driver)}")
        self.log.info(f'title is: {self.driver.title}')
        self.log.info(f"current url is: {self.driver.current_url}")
        loginPage.successful_login("standard_user", "secret_sauce")
        loginPage.logout()

    def test_locked_user_login(self):
        loginPage = LoginPage(self.driver, self.log)
        self.log.info(f"self driver ref is:{id(self.driver)}")
        self.log.info(f'title is: {self.driver.title}')
        self.log.info(f"current url is: {self.driver.current_url}")
        loginPage.locked_user("locked_out_user", "secret_sauce")





