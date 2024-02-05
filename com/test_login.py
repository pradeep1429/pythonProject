import pytest

from demoqa.LoginPage import LoginPage
from utility.Base import Base

@pytest.mark.usefixtures("setup")
class TestBrowser(Base):

    def test_method(self):
        log = self.getLogger()
        loginPage = LoginPage(self.driver,log)
        log.info(f"self driver ref is:{id(self.driver)}")
        log.info(f'title is: {self.driver.title}')
        log.info(f"current url is: {self.driver.current_url}")
        loginPage.open_login_page()
        loginPage.login("testuserr", "Dem0@user")
        loginPage.logout()




