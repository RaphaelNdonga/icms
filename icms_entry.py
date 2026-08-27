import time
from utils import launch_browser, icms_sign_in, manual_type

browser = launch_browser()
page = icms_sign_in(browser)

page.goto("https://icms.kra.go.ke/e-biscus/dispatchAction.action?service=CR&menuReload=true")

declaration_btn = page.locator("#menu112")
declaration_btn.wait_for(state="visible")
declaration_btn.click()

create_imp_cust = page.locator("#msg8066")
create_imp_cust.click()

iframe = page.frame_locator("iframe[refid=msg8066]")
idf_no = iframe.locator("#regno").locator("input")
idf_no.fill("26EMKIM000731139")

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
    browser.close()

display_items = iframe.locator("#tbDisplayIS").locator(".iconBtn")
display_items.click()

iframe.locator("body").evaluate("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(3)

scrollable_list = iframe.locator("#tableItems").locator(".VISUAL_DATACONTAINER")
scrollable_list.evaluate("""
    element => {
        element.scrollTop = element.scrollHeight;
    }
""")

time.sleep(3)

select_switch = iframe.locator("#selectSwitch")
select_switch.click()
# try:
#     first_item = iframe.locator("#row0cell0select")
# except TimeoutError:
#     print("IDF ITEMS NOT FOUND")
#     browser.close()

time.sleep(20)