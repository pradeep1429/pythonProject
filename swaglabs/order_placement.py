from selenium.webdriver.common.by import By


class OrderPlacement:

    ADD_ITEM = (By.ID,"add-to-cart-sauce-labs-backpack")
    REMOVE_ITEM = (By.NAME,"remove-sauce-labs-backpack")
    CHECKOUT_BUTTON = (By.ID,"checkout")
    CART_COUNT = (By.XPATH,"//a[@class='shopping_cart_link']/span")
    FIRST_NAME = (By.ID,"first-name")
    LAST_NAME = (By.ID,"last-name")
    POSTAL_CODE = (By.ID,"postal-code")
    CONTINUE_BUTTON = (By.ID,"continue")
    FINISH_BUTTON = (By.ID,"finish")
    SUCCESS_MESSAGE = (By.XPATH,"//h2[@class='complete-header']")

    def __init__(self, driver,logger):
        self.driver = driver
        self.log = logger


    def add_item_to_cart(self):
        res = False
        try:
            self.driver.find_element(*OrderPlacement.ADD_ITEM).click()
            self.driver.find_element(*OrderPlacement.CART_COUNT).click()
            assert int(self.driver.find_element(*OrderPlacement.CART_COUNT).text).__gt__(0)
            self.log.info("Item added to cart")
            res = True
        except Exception as e:
            self.log.error(f"Item not added to cart: \n{e}")
            return res

    def go_to_checkout(self):
        self.driver.find_element(*OrderPlacement.CHECKOUT_BUTTON).click()
        assert "checkout" in self.driver.current_url, "Checkout page not opened"
        self.log.info("Checkout page opened")

    def enter_checkout_details(**decorator_kwargs):
        def checkout(func):
            def wrapper(self):
                self.driver.find_element(*OrderPlacement.FIRST_NAME).send_keys(decorator_kwargs.get("first_name"))
                self.log.info(f"First names entered as: {decorator_kwargs.get('first_name')}")
                self.driver.find_element(*OrderPlacement.LAST_NAME).send_keys(decorator_kwargs.get('last_name'))
                self.log.info(f"last_name entered as: {decorator_kwargs.get('last_name')}")
                self.driver.find_element(*OrderPlacement.POSTAL_CODE).send_keys(decorator_kwargs.get('postal_code'))
                self.log.info(f"postal_code entered as: {decorator_kwargs.get('postal_code')}")
                result = func(self)
                return result
            return wrapper
        return checkout

    def place_order(self):
        self.driver.find_element(*OrderPlacement.CONTINUE_BUTTON).click()
        self.log.info("Continue button clicked")
        self.driver.find_element(*OrderPlacement.FINISH_BUTTON).click()
        self.log.info("Finish button clicked")
        try:
            assert "Thank you for your order!" in self.driver.find_element(*OrderPlacement.SUCCESS_MESSAGE).text
            self.log.info("Order placed successfully")
        except Exception as e:
            self.log.error(f"Something went wrong, Order not placed:\n {e}")
            assert False

