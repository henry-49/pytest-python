# Network Interception
import pytest
from playwright.sync_api import Page

fakePlayloadOrderResponse = {"data": [], "message": "No Orders"}

# -> api call from browser -> api call contact server return back response to browser -> browser use response to generate html
def intercept_response(route):
    route.fulfill(
        json = fakePlayloadOrderResponse
    )


@pytest.mark.smoke
def test_network_interception1(page:Page):
    # login
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.get_by_placeholder("email@example.com").fill("gregsmith@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    order_text = page.locator(".mt-4").text_content()
    print(order_text)