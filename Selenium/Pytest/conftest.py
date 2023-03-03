import pytest


@pytest.fixture(scope= 'class')
def setup():
    print(" I will be executing first")
    yield
    print(" I will execute last")


@pytest.fixture()
def dataHand():
    print('User profile data is created')
    return ["Salai", "Nivedha", "salanivedha.com"]

@pytest.fixture(params= [("Chrome","Nivedha"), ("Firefox","Salai"), ("Internet Explorer","Arun")])
def crossBrowser(request):
    return request.param

### Git Add, Git Commit, Git Push