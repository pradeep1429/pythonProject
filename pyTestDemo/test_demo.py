
def test_method3():
    str = "hello"
    assert str == "hi","Test failed due to strings not matched"

def test_method4():
    a = 4
    b = 6
    assert a+2 == 6, "Addition did not match"

def test_creditcardinfo():
    print("card method 1 from: {}".format(__name__))