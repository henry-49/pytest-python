# Network Interception
# # maxtobias@gmail.com
from playwright.sync_api import Page, Playwright, expect
from pytest_playwright.pytest_playwright import browser

from utils.api_base import APIUtils


#  https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6777fae6e2b5443b1f10dd10
# -> api call from the browser -> api call contact server return back response to browser -> browser use response to generate html

def intercept_request(route):
    # oder link from Max Tobias and Greg should not be authorize to view this order
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=677e87a4e2b5443b1f19bfa1")

def test_network_interception2(page:Page):
    # login
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)
    page.get_by_placeholder("email@example.com").fill("gregsmith@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    message = page.locator(".blink_me").text_content()
    print(message)


# if goal is to verify if Your Orders text is visible
def test_login_session_storage(playwright: Playwright):
    api_util = APIUtils()
    get_token_value = api_util.get_token(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # script to inject token in session local storage
    page.add_init_script(f"""localStorage.setItem('token','{get_token_value}')""")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text('Your Orders')).to_be_visible()
