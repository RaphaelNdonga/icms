import math
from playwright.sync_api import sync_playwright, Browser
import time
from difflib import SequenceMatcher

LOCATIONS_TO_EXCLUDE = ["CFS", "Full or Empty Yard", "Empty Only Yard"]

def launch_browser() -> Browser:
    return sync_playwright().start().chromium.launch(headless=False, args=["--start-maximized"])

def icms_sign_in(browser:Browser):

    context = browser.new_context(
        no_viewport=True
    )
    page = context.new_page()

    page.goto("https://icms.kra.go.ke/")

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

    return page