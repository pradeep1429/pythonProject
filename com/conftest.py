import configparser
from datetime import datetime

import pytest

from driverManager.driverutils import DriverFactory
from utility.Base import Base


# Fixtures are created when first requested by a test, and are destroyed based on their scope:
# function: the default scope, the fixture is destroyed at the end of the test.
# class: the fixture is destroyed during teardown of the last test in the class.
# module: the fixture is destroyed during teardown of the last test in the module.
# package: the fixture is destroyed during teardown of the last test in the package.
# session: the fixture is destroyed at the end of the test session.

def get_common_info():
    ev = configparser.ConfigParser()
    ev.read(Base.ROOT_PATH + '\\data.ini')
    return ev['common']

@pytest.fixture(scope="class")
def setup(request):
    request.cls.driver = DriverFactory.get_driver(get_common_info().get('browser'))
    request.cls.driver.get(get_common_info().get('base_url'))
    yield
    request.cls.driver.quit()

@pytest.fixture(scope="session")
def setup_session():
    driver = DriverFactory.get_driver(get_common_info().get('browser'))
    driver.get(get_common_info().get('base_url'))
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def test_name(request):
    return request.node.name

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            tc_name = report.nodeid.split("::")[-1]
            file_name = Base.ROOT_PATH+"\\com\\reports\\screenshots\\"+tc_name+ datetime.now().strftime("%Y%m%d_%H_%M_%S") + ".png"
            item.instance.driver.save_screenshot(file_name)
            if file_name:
                html = f'<div><img src="file:{file_name}" alt="screenshot" style="width:600px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>'
                extra.append(pytest_html.extras.html(html))
        report.extra = extra



