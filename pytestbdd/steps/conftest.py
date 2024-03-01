# Fixtures
import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver():
    dri = webdriver.Chrome()
    dri.implicitly_wait(10)
    dri.maximize_window()
    yield dri
    dri.quit()