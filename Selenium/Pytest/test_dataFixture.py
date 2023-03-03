import pytest

from Selenium.Pytest.Baseclass import BaseClass


@pytest.mark.usefixtures("dataHand")
class TestExample(BaseClass):

    def test_editProf(self,dataHand):
        log=self.getlogger()
        log.info(dataHand[0])
        log.info(dataHand[1])
        print(dataHand[2])