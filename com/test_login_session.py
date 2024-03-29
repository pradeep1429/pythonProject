import pytest

from swaglabs.LoginPage import LoginPage
from utility.Base import Base


class TestLoginSession():

    # log = Base.getLogger()
    driver = None

    #@pytest.mark.parametrize("setup_session", "common", indirect=True)
    def test_login_swaglabs(self,setup_session):
        self.driver = setup_session
        log = Base.getLogger()
        loginPage = LoginPage(self.driver,log)
        log.info(f"self driver ref is:{id(self.driver)}")
        log.info(f'title is: {self.driver.title}')
        log.info(f"current url is: {self.driver.current_url}")
        loginPage.successful_login("standard_user", "secret_sauce")
        loginPage.logout()

    @pytest.mark.xfail
    def test_locked_user_login(self,setup_session):
        self.driver = setup_session
        log = Base.getLogger()
        loginPage = LoginPage(self.driver, log)
        log.info(f"self driver ref is:{id(self.driver)}")
        log.info(f'title is: {self.driver.title}')
        log.info(f"current url is: {self.driver.current_url}")
        loginPage.locked_user("locked_out_user", "secret_sauce")






