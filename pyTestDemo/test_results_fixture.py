import pytest

# a global list to store the results (e.g., pass / fail status) of your tests
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

@pytest.mark.usefixtures("update_test_results")
class Testset:
    def test_1(self,update_test_results):
        # add result for this test
        update_test_results("Pass")


    def test_2(self,update_test_results):
        # add result for this test
        update_test_results("Fail")




# class TestCases:
#     def test_6(self, func_list):
#         func_list.append(10)
#
#     def test_7(self, func_list):
#         func_list.append(20)
#
#     def test_8(self, func_list):
#         func_list.append(30)
#
# # conftest.py
#
# @pytest.fixture(scope="session")
# def func_list():
#     ip_list = []
#     yield ip_list
#     print(ip_list)