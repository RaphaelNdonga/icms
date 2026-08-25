import time
from utils import launch_browser, icms_sign_in

browser = launch_browser()
page = icms_sign_in(browser)
time.sleep(5)
page.wait_for_url("https://icms.kra.go.ke/index.jsp")
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
idf_no.fill("12346789")

time.sleep(5)