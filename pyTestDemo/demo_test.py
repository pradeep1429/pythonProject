import configparser

import pytest


#Any pytest file should start with 'test_' or end with '_test'
#PyTest method names should start with 'test'
#Any code should be wrapped in method only
#if two methods have same name last method will overwrite during execution
#to run specific file py.test <filename.py>
# py.test -v -s -n 4 --html=/reports/report.html -> to run tests parallel using pytest-xdist
# pytest -v -s --lf to rerun failed scenarios
def test_method1():
    print("in method 1")

def test_method2():
    print("in method 2")
def get_common_info():
    ev = configparser.ConfigParser()
    ev.read("C:\\Users\\Pradeep_Avadhanam\\Workspace\\pythonProject\\data.ini")
    return ev['common']

@pytest.fixture
def get_info():
        ev = configparser.ConfigParser()
        ev.read("C:\\Users\\Pradeep_Avadhanam\\Workspace\\pythonProject\\data.ini")
        result = ev["common"]
        return result

# def test_fix(get_info):
#     print(get_info.get("browser"))

