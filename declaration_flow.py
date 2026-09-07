import time
from utils import launch_browser, icms_sign_in
from search_entry import search_entry
from general_seg.details_tab import details_tab
from general_seg.movements_tab import movements_tab

browser = launch_browser()
page = icms_sign_in(browser)

search_entry(page, "26EMKIM401078120")
details_tab(page)
movements_tab(page)
time.sleep(20)
