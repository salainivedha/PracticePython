#Any pytest file should start with test_ or end with _test
# Pytest method names should start with test
# Any code should be wrapped in method only
# Method name should have sense
# -k stands for method name execution
# -s logs in o/p
#-v for more info in metadata
# you can run specific file with py.test<filename>
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "hello"
    assert msg == 'Hi', "Test failed because condition does not match"

def test_SecondProgram():
    a = 4
    b = 6
    assert a+2 == 6, "Addition does not match"




