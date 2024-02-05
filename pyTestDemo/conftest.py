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