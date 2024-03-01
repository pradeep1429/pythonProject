from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

DUCKDUCKGO_HOME = 'https://duckduckgo.com/'

scenarios('../features/search.feature')




@given('the DuckDuckGo home page is displayed')
def ddg_home(driver):
    driver.get(DUCKDUCKGO_HOME)

@when(parsers.parse('the user searches for "{phrase}"'))
def search_phrase(driver, phrase):
    search_input = driver.find_element(By.ID,'searchbox_input')
    search_input.send_keys(phrase + Keys.RETURN)

@then(parsers.parse('results are shown for "{phrase}"'))
def search_results(driver, phrase):
    assert len(driver.find_elements(By.XPATH,'//div')) > 0
    search_input = driver.find_element(By.ID,'search_form_input')
    assert search_input.get_attribute('value') == phrase