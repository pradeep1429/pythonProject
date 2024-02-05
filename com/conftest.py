
import pytest
from datetime import datetime
from driverManager.driverutils import DriverFactory
from utility.Base import Base


# Fixtures are created when first requested by a test, and are destroyed based on their scope:
# function: the default scope, the fixture is destroyed at the end of the test.
# class: the fixture is destroyed during teardown of the last test in the class.
# module: the fixture is destroyed during teardown of the last test in the module.
# package: the fixture is destroyed during teardown of the last test in the package.
# session: the fixture is destroyed at the end of the test session.


@pytest.fixture(scope="class")
def setup(request):
    request.cls.driver = DriverFactory.get_driver("chrome")
    request.cls.driver.get("https://demoqa.com/books")
    yield
    request.cls.driver.close()

@pytest.fixture(scope="module")
def test_name(request):
    return request.node.name

#Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.:param item:
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



