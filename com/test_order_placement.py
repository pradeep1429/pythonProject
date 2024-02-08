
from swaglabs.LoginPage import LoginPage
from swaglabs.order_placement import OrderPlacement
from utility.Base import Base

class TestOrderPlacement():
    log = Base.getLogger()
    driver = None

    def test_order_placement(self, setup_session):
        self.driver = setup_session
        loginPage = LoginPage(self.driver,self.log)
        order = OrderPlacement(self.driver,self.log)
        self.log.info(f"self driver ref is:{id(self.driver)}")
        self.log.info(f'title is: {self.driver.title}')
        self.log.info(f"current url is: {self.driver.current_url}")
        loginPage.login("standard_user", "secret_sauce")
        order.add_item_to_cart()
        order.go_to_checkout()
        self.order_placement()
        loginPage.logout()

    def test_order_placement_error(self, setup_session):
        self.driver = setup_session
        loginPage = LoginPage(self.driver, self.log)
        order = OrderPlacement(self.driver, self.log)
        self.log.info(f"self driver ref is:{id(self.driver)}")
        self.log.info(f'title is: {self.driver.title}')
        self.log.info(f"current url is: {self.driver.current_url}")
        loginPage.login("error_user", "secret_sauce")
        order.add_item_to_cart()
        order.go_to_checkout()
        self.order_placement()
        loginPage.logout()

    @OrderPlacement.enter_checkout_details(first_name="test",last_name="user",postal_code=23423)
    def order_placement(self):
        order = OrderPlacement(self.driver, self.log)
        order.place_order()