import pytest

@pytest.fixture(scope="session") # scope=class is the same at scope=moudle
def preStepupWork():
    print("I setup browser instance")