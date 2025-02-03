#E2E API Test
# playwright codegen https://rahulshettyacademy.com/client
# Username: gregsmith@gmail.com
# password: Iamking@000
import json

# pytest --browser_name firefox  -m smoke -n 3 --tracing on --html=report.html

import pytest
from playwright.sync_api import Playwright, expect

from pageObjects.login import LoginPage
from pageObjects.dashboard import DashboardPage
from utils.api_base_framework import APIUtils

# Json file -> util-> access into test
with open('data/credentials.json') as f:
    test_date = json.load(f)
    print(test_date)
    user_credential_list = test_date['user_credentials']

@pytest.mark.smoke
@pytest.mark.parametrize('user_credential_data', user_credential_list)
def test_e2e_web_api(playwright: Playwright, browser_instance, user_credential_data):
    user_email = user_credential_data["userEmail"]
    user_password = user_credential_data["userPassword"]
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # page = context.new_page()  # from here is linking to everywhere on the page

    # create order -> orderId
    api_utils = APIUtils()
    orderId = api_utils.create_order(playwright, user_credential_data)

    #login
    login_page = LoginPage(browser_instance) # object for login page class
    login_page.navigate()
    # Dashboard Page
    dashboard_page = login_page.login(user_email, user_password)
    # dashboard_page = DashboardPage(page)

    # Orders History Page -> Order is present
    order_history_page = dashboard_page.select_orders_navigation_link()
    order_detail_page = order_history_page.select_order(orderId)
    order_detail_page.verify_order_message()

    # context.close()
