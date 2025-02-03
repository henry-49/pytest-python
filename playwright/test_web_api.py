#E2E API Test
# playwright codegen https://rahulshettyacademy.com/client
# Username: gregsmith@gmail.com
# password: Iamking@000
from playwright.sync_api import Playwright, expect

from utils.api_base import APIUtils


def test_e2e_web_api(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # create order -> orderId
    api_utils = APIUtils()
    orderId = api_utils.create_order(playwright)

    #login
    page.goto("https://rahulshettyacademy.com/client")
    # page.get_by_placeholder("email@example.com").fill("gregsmith@gmail.com")
    page.locator("#userEmail").fill("gregsmith@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()


    # orders history page -> order is present
    page.get_by_role("button", name="ORDERS").click()
    order_row = page.locator("tr", has_text=orderId)
    order_row.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")

    context.close()
