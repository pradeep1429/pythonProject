from swaglabs.LoginPage import LoginPage
from swaglabs.order_placement import OrderPlacement
from utility.Base import Base
from utility.ExcelReader import excel_to_dict


class TestExcelOrderPlacement():
    test_data = excel_to_dict(Base.ROOT_PATH + "\\test_data.xlsx", "Sheet1")
    log = Base.getLogger()
    driver = None

    def test_order_placement(self, setup_session):
        self.driver = setup_session
        print(self.test_data)
        for data in self.test_data:
            login_page = LoginPage(self.driver,self.log)
            order = OrderPlacement(self.driver,self.log)
            self.log.info(f"self driver ref is:{id(self.driver)}")
            self.log.info(f'title is: {self.driver.title}')
            self.log.info(f"current url is: {self.driver.current_url}")
            login_page.login(data.get("user_name"), data.get("password"))
            if order.add_item_to_cart() is False:
                self.log.error(f"iteration {data} failed")
                continue
            order.go_to_checkout()
            self.order_placement()
            login_page.logout()



    @OrderPlacement.enter_checkout_details(first_name="test",last_name="user",postal_code=23423)
    def order_placement(self):
        order = OrderPlacement(self.driver, self.log)
        order.place_order()