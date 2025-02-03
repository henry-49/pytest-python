# UI Validation
from playwright.sync_api import Page, expect


def test_ui_validation_dynamic_script(page:Page):
    # product: add iphone X , Nokia Edge  -> verify 2 items are showing in cart
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    iphone_x = page.locator("app-card").filter(has_text="iphone X")
    iphone_x.get_by_role("button").click()
    nokia_edge = page.locator("app-card").filter(has_text="Nokia Edge")
    nokia_edge.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)



def test_child_window_handle(page:Page):
    # QA Meetup with Rahul Shetty @Bangalore - Limited Seats! Book Now!
    # mentor@rahulshettyacademy.com
    page.goto("https://rahulshettyacademy.com/loginpagePractise")

    with page.expect_popup() as new_page_info:
        page.locator(".blinkingText").filter(has_text="Free Access to InterviewQues/ResumeAssistance/Material").click() # new page
        child_page = new_page_info.value
        text = child_page.locator(".red").text_content()
        print(text)
        words = text.split("at")
        email = words[1].strip().split(" ")[0]
        assert email == "mentor@rahulshettyacademy.com"
        print(email)
