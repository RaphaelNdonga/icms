from dataclasses import dataclass
import json
import math
from playwright.sync_api import sync_playwright, Browser, Locator, Page, TimeoutError
import time
from difflib import SequenceMatcher

def launch_browser() -> Browser:
    return sync_playwright().start().chromium.launch(headless=False, args=["--start-maximized"])

def icms_sign_in(browser:Browser):

    context = browser.new_context(
        no_viewport=True,
        storage_state="storage_state.json"
    )
    page = context.new_page()

    icms_page = ICMS_PAGES[1]
    icms_main_page = icms_page.login_page.url
    home_page = "https://icms.kra.go.ke/index.jsp"

    page.goto(icms_main_page)

    try:
        page.wait_for_url(home_page, timeout=3)

    except TimeoutError:
        username = page.locator("#username")
        username.fill("CSAP000620077QX")

        password = page.locator(icms_page.login_page.password_id)
        password.fill("Wabwoba@2025")

        captcha_input = page.locator("#captcha")

        captcha_expression = page.locator("#captchaExpression")
        captcha_text = captcha_expression.text_content()

        num1, num2 = captcha_text.split("+")
        num2 = num2.replace("=?", "")
        answer = int(num1) + int(num2)

        captcha_input.fill(str(answer))

        login_btn = page.locator("#loginBtn")
        login_btn.click()

        time.sleep(1)
        force_login_btn = page.locator("button").get_by_text("OK")
        if force_login_btn.is_visible():
            force_login_btn.click()

        page.wait_for_url(home_page)

        # storage_state = context.storage_state()

        # with open("storage_state.json", "w") as f:
        #     json.dump(storage_state, f, indent=4)

    return page

def manual_type(page:Page, input_el:Locator, word:str):
    input_el.click()

    for c in word:
        page.keyboard.press(c)

def manual_del(input_el:Locator):
    input_el.click()
    input_el.clear()

@dataclass
class LoginPage:
    url: str
    password_id: str

@dataclass
class IcmsPage:
    login_page: LoginPage

ICMS = IcmsPage(login_page=LoginPage(url="https://icms.kra.go.ke/index.jsp", password_id="#passwd"))
ICMSCAS = IcmsPage(login_page=LoginPage(url="https://icmscas.kra.go.ke/cas/login?service=https%3A%2F%2Ficms.kra.go.ke%2F", password_id="#password"))
ICMS_PAGES = [ICMS, ICMSCAS]