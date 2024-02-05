import pytest


@pytest.mark.usefixtures("dataLoad")
class TestFixtures:

    def test_method(self,dataLoad):
         for i in dataLoad:
             print(i)
