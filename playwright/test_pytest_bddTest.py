from typing import Any

import pytest
from pyexpat import features
from pytest_bdd import given, when, then, parsers, scenarios

from pageObjects.login import LoginPage
from utils.api_base_framework import APIUtils

scenarios('features/orderTransaction.feature')
@pytest.fixture
def shared_data():
    return {}

@given(parsers.parse('place the item order with {username} and {password}'))
def place_item_order(playwright, username, password, shared_data):
    user_credential_data = {"userEmail": username, "userPassword": password}
    api_utils = APIUtils()
    orderid = api_utils.create_order(playwright, user_credential_data)
    shared_data['order_id'] = orderid



@given("the user is on landing page")
def user_on_landing_page(browser_instance, shared_data):
    loginpage = LoginPage(browser_instance)  # object for login page class
    loginpage.navigate()
    shared_data['login_page'] = loginpage


@when(parsers.parse('I login to portal with {username} and {password}'))
def login_to_portal(username, password, shared_data):
    loginpage = shared_data['login_page']
    dashboardpage = loginpage.login(username, password)
    shared_data['dashboard_page'] = dashboardpage

@when("navigate to orders page")
def navigate_to_orders_page(shared_data):
    dashboard_page = shared_data['dashboard_page']
    order_history_page = dashboard_page.select_orders_navigation_link()
    shared_data['order_history_page'] = order_history_page

@when("select the orderId")
def select_order_id(shared_data):
    orderhistorypage = shared_data['order_history_page']
    orderid = shared_data['order_id']
    orderdetailpage = orderhistorypage.select_order(orderid)
    shared_data['order_detail_page'] = orderdetailpage


@then('order message is successfully displayed')
def order_message_successfuly_displayed(shared_data):
    orderdetailpage = shared_data['order_detail_page']
    orderdetailpage.verify_order_message()
