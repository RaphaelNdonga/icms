import time
from utils import launch_browser, icms_sign_in, manual_type

browser = launch_browser()
page = icms_sign_in(browser)

page.goto("https://icms.kra.go.ke/e-biscus/dispatchAction.action?service=CR&menuReload=true")

declaration_btn = page.locator("#menu112")
declaration_btn.wait_for(state="visible")
declaration_btn.click()

search_menu = page.locator("#msg10135").locator("a")
search_menu.click()

iframe = page.frame_locator("iframe[refid=msg10135]")
reg_no_input = iframe.locator("#Field12232").locator("input")
reg_no_input.fill("26EMKIM401078120")

search_btn = iframe.locator("#But8486")
search_btn.click()

first_search_result = iframe.locator("#row0cell0Col9280")
first_search_result.click()

process_btn = iframe.locator("#tbProcess").locator(".iconBtn")
process_btn.click()

time.sleep(20)