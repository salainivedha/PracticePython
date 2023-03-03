#Any pytest file should start with test_ or end with _test
# Pytest method names should start with test
# Any code should be wrapped in method only
# Method name should have sense
# -k stands for method name execution
# -s logs in o/p
#-v for more info in metadata
# you can run specific file with py.test<filename>
import pytest


@pytest.mark.usefixtures("setup")
class Test_Example:
    def test_FixtureDemo(self):
        print(" I will execute my Fixture Demo")

    def test_FixtureDemo1(self):
        print(" I will execute my Fixture Demo1")
    def test_FixtureDemo2(self):
        print(" I will execute my Fixture Demo2")

    def test_FixtureDemo3(self):
        print(" I will execute my Fixture Demo3")