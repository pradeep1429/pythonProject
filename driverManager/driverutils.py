from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService


class DriverFactory:
    _instances = {}

    def __new__(cls,browser):
        if browser not in cls._instances:
            instance = super().__new__(cls)
            match browser.lower():
                case "chrome":
                    instance.driver = webdriver.Chrome(service=ChromeService())
                case "firefox":
                    instance.driver = webdriver.Firefox(service=FirefoxService())
                case _:
                    raise Exception(f'Browser {browser} not supported')

            instance.driver.implicitly_wait(30)
            instance.driver.maximize_window()
            instance.driver.set_page_load_timeout(5000)
            cls._instances[browser] = instance
        return cls._instances[browser]

    @classmethod
    def get_driver(cls,browser):
        return cls(browser).driver

