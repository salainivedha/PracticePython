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
def test_firstProgram(setup):
    print("hello")

@pytest.mark.xfail
def test_SecondGreet():
    print("good morning")




