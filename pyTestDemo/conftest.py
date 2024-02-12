import pytest


@pytest.fixture(scope="class")
def setup():
    print("setup executed first")
    yield
    print("this will execute last")

@pytest.fixture()
def dataLoad():
    print("this is dataload")
    return ["python","incubation","in","8weeks"]

@pytest.fixture(params=["chrome","firefox","ie"])
def crossBrowser(request):
    return request.param

test_results = []
@pytest.fixture
def update_test_results(request):
    # using request.node to access the current test node
    test_name = request.node.nodeid

    def _add_result(status):
        test_results.append((test_name, status))

    yield _add_result

    # Optional: print results after all tests
    if request.node == request.session.items[-1]:
        for name, status in test_results:
            print(f"{name}: {status}")
@pytest.fixture
def username():
    return 'username'

class TestPlugin:
    def __init__(self):
        self.failed_tests = []

    @pytest.hookimpl(tryfirst=True, hookwrapper=True)
    def pytest_runtest_makereport(self, item, call):
        # execute all other hooks to obtain the report object
        outcome = yield
        rep = outcome.get_result()

        # check if test has failed
        if rep.when == "call" and rep.failed:
            # add the failed test name to the list
            self.failed_tests.append(item)
            print(f"Encountered a failed test: {item.nodeid}")

@pytest.fixture(scope="session", autouse=True)
def start_plugin(pytestconfig):
    test_plugin = TestPlugin()
    pytestconfig.pluginmanager.register(test_plugin)
    return pytestconfig