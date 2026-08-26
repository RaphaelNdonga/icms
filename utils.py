import json
import math
from playwright.sync_api import sync_playwright, Browser
import time
from difflib import SequenceMatcher

LOCATIONS_TO_EXCLUDE = ["CFS", "Full or Empty Yard", "Empty Only Yard"]

def launch_browser() -> Browser:
    return sync_playwright().start().chromium.launch(headless=False, args=["--start-maximized"])

def icms_sign_in(browser:Browser):

    context = browser.new_context(
        no_viewport=True,
        storage_state="storage_state.json"
    )
    page = context.new_page()

    icms_main_page = "https://icms.kra.go.ke/"
    home_page = "https://icms.kra.go.ke/index.jsp"

    page.goto(icms_main_page)

    page.wait_for_url(home_page, timeout=3)

    if page.url != home_page:
        username = page.locator("#username")
        username.fill("CSAP000620077QX")

        password = page.locator("#passwd")
        password.fill("Wabwoba@2023")

        captcha_input = page.locator("#captcha")

        captcha_expression = page.locator("#captchaExpression")
        captcha_text = captcha_expression.text_content()

        num1, num2 = captcha_text.split("+")
        num2 = num2.replace("=?", "")
        answer = int(num1) + int(num2)

        captcha_input.fill(str(answer))

        login_btn = page.locator("#loginBtn")
        login_btn.click()

        page.wait_for_url(home_page, timeout=5)

        storage_state = context.storage_state()

        with open("storage_state.json", "w") as f:
            json.dump(storage_state, f, indent=4)

    return page