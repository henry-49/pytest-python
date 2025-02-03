from email.policy import default

import pytest

# request is use to access globally configured variable also local test variable
# session will run once before wohel executions begins

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome",  help="browser selection"
    )

    parser.addoption(
        "--url_name", action="store", default="https://rahulshettyacademy.com/client", help="browser selection"
    )

@pytest.fixture(scope="session")
def user_credential_data(request):
    return request.param

@pytest.fixture
def browser_instance(playwright, request):
    # get request on a global level
    browser_name = request.config.getoption("browser_name")
    url_name = request.config.getoption("url_name")
    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
         browser = playwright.firefox.launch(headless=False)


    context = browser.new_context()
    page = context.new_page()  # from here is linking to everywhere on the page
    # page.goto(url_name)
    yield page
    context.close()
    browser.close()