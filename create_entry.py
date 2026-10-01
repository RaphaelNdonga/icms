import time
from utils import launch_browser, icms_sign_in, manual_type
from playwright.sync_api import Page, expect, Locator

def create_entry(page:Page, idf_no: str):
    page.goto("https://icms.kra.go.ke/e-biscus/dispatchAction.action?service=CR&menuReload=true")

    declaration_btn = page.locator("#menu112")
    declaration_btn.wait_for(state="visible")
    declaration_btn.click()

    create_imp_cust = page.locator("#msg8066")
    create_imp_cust.click()

    iframe = page.frame_locator("iframe[refid=msg8066]")
    idf_no_input = iframe.locator("#regno").locator("input")
    idf_no_input.fill(idf_no)

    custom_office = iframe.locator("#customOffice").locator("input").first
    manual_type(page, custom_office, "EMK")

    time.sleep(2)

    national_subdivision = iframe.locator("#nationalSubdivision").locator("input").first
    manual_type(page, national_subdivision, "ICD")

    search_idf_btn = iframe.locator("#searchIDF")
    search_idf_btn.click()

    idf_approval = iframe.locator("#row0cell1Col9281")

    if idf_approval.text_content() == "IDF approved":
        idf_approval.click()
    else:
        print("IDF NOT APPROVED")
        return ""

    display_items = iframe.locator("#tbDisplayIS").locator(".iconBtn")
    display_items.click()

    iframe.locator("body").evaluate("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(3)

    scrollable_list = iframe.locator("#tableItems").locator(".VISUAL_DATACONTAINER")
    gradual_top_bottom_scroll(page, scrollable_list)

    select_switch = iframe.locator("#selectSwitch")
    select_switch.click()

    first_item = iframe.locator("#row0cell0select").locator("input")
    expect(first_item).to_be_checked(timeout=30000)

    create_btn = iframe.locator("#tbProcess").locator(".iconBtn")
    create_btn.click()

    entry_iframe = page.locator("#form-tabs-iframeArea").frame_locator("iframe").last

    declaration_no = entry_iframe.locator("#Field8777")

    declaration_no.wait_for(state="visible")

    entry_no = declaration_no.locator("input").first.input_value()

    return entry_no

def gradual_top_bottom_scroll(page: Page, scrollable_list:Locator):
    scrollable_list.evaluate("""
        element => {
            element.scrollTop = element.scrollHeight;
        }
    """)
    time.sleep(1)
    scrollable_list.evaluate("""
        element => {
            element.scrollTop = 0;
        }
    """)   
    time.sleep(1)
    while True:
        previous_top = scrollable_list.evaluate("el => el.scrollTop")

        scrollable_list.evaluate("""
            element => {
                element.scrollTop += 100;
            }
        """)

        page.wait_for_timeout(200)

        current_top = scrollable_list.evaluate("el => el.scrollTop")

        if current_top == previous_top:
            break

