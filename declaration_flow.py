import time
from utils import launch_browser, icms_sign_in, manual_type
from search_entry import search_entry
from general_seg import details_tab

browser = launch_browser()
page = icms_sign_in(browser)

search_entry(page, "26EMKIM401078120")
details_tab(page)
time.sleep(20)
