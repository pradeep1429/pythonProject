import pytest


# This fixture is executed once per function
@pytest.fixture(scope='function')
def function_fixture():
    print("Setting up a function-level fixture")
    yield
    print("Tearing down a function-level fixture")


# This fixture is executed once per class
@pytest.fixture(scope='class')
def class_fixture():
    print("Setting up a class-level fixture")
    yield
    print("Tearing down a class-level fixture")


# This fixture is executed once per module
@pytest.fixture(scope='module')
def module_fixture():
    print("Setting up a module-level fixture")
    yield
    print("Tearing down a module-level fixture")

# This fixture is executed once per package
@pytest.fixture(scope='package')
def package_fixture():
    print("Setting up a package-level fixture")
    yield
    print("Tearing down a package-level fixture")


# This fixture is executed once per session
@pytest.fixture(scope='session')
def session_fixture():
    print("Setting up a session-level fixture")
    yield
    print("Tearing down a session-level fixture")


class TestExample:

    def test_1(self, function_fixture, class_fixture, module_fixture, package_fixture, session_fixture):
        print("Executing test 1")

    def test_2(self, function_fixture, class_fixture, module_fixture, package_fixture, session_fixture):
        print("Executing test 2")


def test_3(function_fixture, class_fixture, module_fixture, package_fixture, session_fixture):
    print("Executing test 3")