#Fixtures
import pytest


@pytest.fixture(scope="module") # scope=class is the same at scope=moudle
def preWork():
    print("I setup moudle instance in preWork")
    return "pass"

@pytest.fixture(scope="function") # scope=class is the same at scope=moudle
def secondWork():
    print("I setup function instance in secondWork")
    yield # it will pause here
    print("tear down validation") # can also close database connection here


@pytest.mark.smoke
def test_initialCheck(preWork, secondWork):
    print("This is first test")
    assert preWork == "pass"

@pytest.mark.skip
def test_secondCheck(preStepupWork, secondWork):
    print("This is second test")