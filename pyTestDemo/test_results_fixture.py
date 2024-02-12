import pytest

@pytest.mark.usefixtures("update_test_results")
class Testset:
    def test_1(self,update_test_results):
        # add result for this test
        update_test_results("Pass")


    def test_2(self,update_test_results):
        # add result for this test
        update_test_results("Fail")




