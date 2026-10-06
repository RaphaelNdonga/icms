import json
import time
from utils import launch_browser, icms_sign_in, LpDetails
from search_entry import search_entry
from general_seg.details_tab import details_tab
from general_seg.movements_tab import movements_tab
from general_seg.transport_tab import transport_tab
from items_seg.details_tab import item_details_tab
from items_seg.packages_tab import packages_tab
from items_seg.attachments_tab import attachments_tab
from create_entry import create_entry
from dataclasses import asdict

browser = launch_browser()
page = icms_sign_in(browser)

# IDF_NUMBER = "26MBAIM004065737"

# entry_no = create_entry(page, IDF_NUMBER)

# if not entry_no:
#     browser.close()

# print("Entry no: ", entry_no)

# entry_no = "26EMKIM401240252"
# search_entry(page, entry_no)
search_entry(page, "26EMKIM401236921", settled = True)
# details_tab(page)
# movements_tab(page)

# iframe = page.locator("#form-tabs-iframeArea").frame_locator("iframe").last

# items_radio = iframe.locator("#Field8462").locator("input")
# items_radio.click()

# item_details_tab(page, 0)


list_lp_details = transport_tab(page, settled=True)

lp_json = json.dumps([asdict(lp) for lp in list_lp_details], indent=2)

with open("lp.json", "w") as file:
    file.write(lp_json)

# packages_tab(page, 0, lp_details)

# attachments_tab(page)

time.sleep(2000)
