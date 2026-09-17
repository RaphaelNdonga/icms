import time
from utils import launch_browser, icms_sign_in
from search_entry import search_entry
from general_seg.details_tab import details_tab
from general_seg.movements_tab import movements_tab
from general_seg.transport_tab import transport_tab

browser = launch_browser()
page = icms_sign_in(browser)

# Entry of interest: 26EMKIM401055916
# search_entry(page, "26EMKIM401078120")
search_entry(page, "26EMKIM401055916", settled = True)
# details_tab(page)
# movements_tab(page)
transport_tab(page, settled=True)

time.sleep(20)
