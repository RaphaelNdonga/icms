import json
import time
from utils import launch_browser, icms_sign_in

browser = launch_browser()
page = icms_sign_in(browser)

page.goto("https://icms.kra.go.ke/e-biscus/dispatchAction.action?service=CR&menuReload=true")
time.sleep(5)

declaration_btn = page.locator("#menu112")
declaration_btn.wait_for(state="visible")
declaration_btn.click()

create_imp_cust = page.locator("#msg8066")
create_imp_cust.click()

time.sleep(5)

iframe = page.frame_locator("iframe[refid=msg8066]")
idf_no = iframe.locator("#regno").locator("input")
idf_no.fill("26EMKIM000731139")

click_out_section = iframe.locator(".w-label4").first

custom_office = iframe.locator("#customOffice").locator("input").first
custom_office.fill("EMK")
click_out_section.click()
time.sleep(1)
custom_office.click()

national_subdivision = iframe.locator("#nationalSubdivision").locator("input").first
national_subdivision.click()
national_subdivision.fill("ICD")

click_out_section.click()
time.sleep(1)
national_subdivision.click()

search_idf_btn = iframe.locator("#searchIDF")
search_idf_btn.click()

time.sleep(20)