import pytest


@pytest.mark.parametrize("i", range(30))
def test_num(i):
    if i in (14, 29):
        pytest.fail("test failed...")