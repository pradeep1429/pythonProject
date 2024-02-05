# tests can be marked with tag by @pytest.mark.mark_name and then run with -m
#to ignore result in log @pytest.mark.xfail
import pytest

@pytest.mark.smoke
def test_method1():
    print("method 1 with tag smoke")

@pytest.mark.smoke
@pytest.mark.skip
def test_method2():
    print("method 2 with tag smoke")
    a = 4
    b = 6
    assert b + 2 == 6, "Addition did not match"


@pytest.mark.regression
def test_method4():
    print("method 4 with tag regression")

@pytest.mark.regression
def test_method5():
    print("method 5 with tag regression")
