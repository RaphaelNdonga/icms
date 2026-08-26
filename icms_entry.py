import time
from utils import launch_browser, icms_sign_in, manual_type

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

custom_office = iframe.locator("#customOffice").locator("input").first
manual_type(page, custom_office, "EMK")


national_subdivision = iframe.locator("#nationalSubdivision").locator("input").first
manual_type(page, national_subdivision, "ICD")

search_idf_btn = iframe.locator("#searchIDF")
search_idf_btn.click()

time.sleep(20)