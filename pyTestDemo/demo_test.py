
#Any pytest file should start with 'test_' or end with '_test'
#PyTest method names should start with 'test'
#Any code should be wrapped in method only
#if two methods have same name last method will overwrite during execution
#to run specific file py.test <filename.py>
# py.test -v -s -n 4 --html=/reports/report.html -> to run tests parallel using pytest-xdist
def test_method1():
    print("in method 1")

def test_method2():
    print("in method 2")



