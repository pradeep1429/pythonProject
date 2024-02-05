#pytest -k creditcard -v -s
#this will run the tests with method name contains 'creditcard'

def test_creditcardinfo():
    print("card method 1")

def test_creditcard2():
    print("credit card 2")

def test_Credit_Card():
    print("credit card 3 not executed")
def test_creditcard():
    print("credit card 4")
def creditcard_test():
    print("credit card 5 not executed due to method name not started with test")
