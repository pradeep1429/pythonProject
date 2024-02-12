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

def ini_loader(section):
    def decorator(func):
        def wrapper(*args, **kwargs):
            parser = configparser.ConfigParser()
            parser.read(Base.ROOT_PATH + '\\data.ini')
            kwargs[section] = dict(parser.items(section))
            return func(*args, **kwargs)
        return wrapper
    return decorator

@pytest.fixture(scope="class")
def setup(request):
    request.cls.driver = DriverFactory.get_driver(get_common_info().get('browser'))
    request.cls.driver.get(get_common_info().get('base_url'))
    yield
    request.cls.driver.quit()

# @pytest.fixture(scope="session")
# @ini_loader("common")
# def setup_session(common):
#     driver = DriverFactory.get_driver(common.get('browser'))
#     driver.get(common.get('base_url'))
#     yield driver
#     driver.quit()

@pytest.fixture(scope="session")
def setup_session():
    driver = DriverFactory.get_driver(get_common_info().get('browser'))
    driver.get(get_common_info().get('base_url'))
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def test_name(request):
    return request.node.name

# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             tc_name = report.nodeid.split("::")[-1]
#             file_name = Base.ROOT_PATH+"\\com\\reports\\screenshots\\"+tc_name+ datetime.now().strftime("%Y%m%d_%H_%M_%S") + ".png"
#             item.instance.driver.save_screenshot(file_name)
#             if file_name:
#                 html = f'<div><img src="file:{file_name}" alt="screenshot" style="width:600px;height:228px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>'
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra

class TestPlugin:
    def __init__(self):
        self.failed_tests = []

    @pytest.hookimpl(tryfirst=True, hookwrapper=True)
    def pytest_runtest_makereport(self, item, call):
        #'item': It represents a single test item (a test function or method).
        # An item is characterized by its nodeid which denotes a file-system-like path from the collection root down to the test, for example "test_folder/test_file.py::test_func".
        # It's an instance of _pytest.nodes.Item class.
        #'call': A CallInfo instance that encapsulates the results of invoking a test function/method. CallInfo has the following attributes:
        # execute all other hooks to obtain the report object
        pytest_html = item.config.pluginmanager.getplugin('html')
        outcome = yield
        report = outcome.get_result()
        extra = getattr(report, 'extra', [])
        # check if test has failed
        if report.when == 'call' or report.when == "setup":
            xfail = hasattr(report, 'wasxfail')
            if (report.skipped and xfail) or (report.failed and not xfail):
                # add the failed test name to the list
                self.failed_tests.append(item)
                print(f"Encountered a failed test: {item.nodeid}")
                tc_name = report.nodeid.split("::")[-1]
                file_name = Base.ROOT_PATH + "\\com\\reports\\screenshots\\" + tc_name + datetime.now().strftime(
                    "%Y%m%d_%H_%M_%S") + ".png"
                item.instance.driver.save_screenshot(file_name)
                if file_name:
                    html = f'<div><img src="file:{file_name}" alt="screenshot" style="width:600px;height:228px;" ' \
                           'onclick="window.open(this.src)" align="right"/></div>'
                    extra.append(pytest_html.extras.html(html))
            report.extra = extra

@pytest.fixture(scope="session", autouse=True)
def start_plugin(pytestconfig):
    test_plugin = TestPlugin()
    pytestconfig.pluginmanager.register(test_plugin)
    return pytestconfig


# Use fixtures when:
# You want to set up and tear down code for tests, such as: setting up database connections, creating a temporary file or directory, initializing certain variables, etc.
# You need to share data or state among multiple tests.
# You require a modular and scalable setup for your tests. Fixtures can be used in other fixtures, in tests, and even in conftest.py for code reusability.
# Explicit usage needs to be shown. Fixtures need to be declared either in the test function arguments or with pytest.mark.usefixtures hence it's clear to see where they are being used.
#
# Use hooks when:
# You need to customize or manipulate the behavior of pytest itself, such as: changing how pytest discovers tests, adding command line options, handling logging, or modifying the test report.
# The action needs to be done once per session or per module, such as starting up a browser just once for a series of tests (you can use fixtures to do this as well, but a session or module scoped hook can be a cleaner approach).
# Implicit changes need to be done across multiple tests, modules or the whole test suite.
# You want to add or custom handle failures, warnings, errors or reports.
# In summary, hooks influence the general pytest execution process, and provide implicit, global-level changes. Fixtures, however, are used for more local, explicit actions – influencing tests directly or providing data for tests.
