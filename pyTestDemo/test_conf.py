import pytest

# def test_username(username):
#     assert username == 'username'

@pytest.fixture
def username(username):
    return 'overridden-' + username


def test_username(username):
    assert username == 'overridden-username'

@pytest.fixture
def username(username):
    return 'overridden-else-' + username


