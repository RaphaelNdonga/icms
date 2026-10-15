import json
import time
from utils import launch_browser, icms_sign_in, manual_type, manual_del
from search_entry import search_entry
from general_seg.details_tab import details_tab
from general_seg.movements_tab import movements_tab
from general_seg.transport_tab import transport_tab
from items_seg.details_tab import item_details_tab
from items_seg.packages_tab import packages_tab
from items_seg.attachments_tab import attachments_tab
from create_entry import create_entry
from dataclasses import asdict
from generation_models import ENTRY_ITEMS
from playwright.sync_api import expect

browser = launch_browser()
page = icms_sign_in(browser)

# IDF_NUMBER = "26MBAIM004065737"

# entry_no = create_entry(page, IDF_NUMBER)

# if not entry_no:
#     browser.close()

# print("Entry no: ", entry_no)

print("entry items length: ", len(ENTRY_ITEMS.entry_items))

entry_no = "26EMKIM401240252"
search_entry(page, entry_no)
# search_entry(page, "26EMKIM401236921", settled = True)
# details_tab(page)
# movements_tab(page)

iframe = page.locator("#form-tabs-iframeArea").frame_locator("iframe").last

items_radio = iframe.locator("#Field8462").locator("input")
items_radio.click()


for i in range(len(ENTRY_ITEMS.entry_items)):
    entry_item = ENTRY_ITEMS.entry_items[i]

    item_number_input = iframe.locator("#List8905").locator("input").last
    expect(item_number_input).to_be_editable(timeout=10000)
    str_num = str(entry_item.idf_item_number)

    while len(str_num) < 3:
        str_num = "0" + str_num

    while item_number_input.input_value() != str_num:
        manual_del(item_number_input)
        print(f"str_num is {str_num} while input value is: {item_number_input.input_value()}... trying again")
        manual_type(page, item_number_input, str_num)
        click_out = iframe.locator(".ui_list_ListOfValue_button").first.click()
        time.sleep(2)
        display_item_btn = iframe.locator("#But7987")
        display_item_btn.click()
        time.sleep(2)

    # delete_item_btn = iframe.locator("#But7943")

    item_details_tab(page, i)

    entry_pkgs = entry_item.packages
    for j in range(len(entry_pkgs)):
        packages_tab(page, j, entry_pkgs[j])

    if i == 0:
        attachments_tab(page)


# list_lp_details = transport_tab(page, settled=True)

# print("lp items: ", len(list_lp_details))

# lp_json = json.dumps([asdict(lp) for lp in list_lp_details], indent=2)

# with open("lp.json", "w") as file:
#     file.write(lp_json)


time.sleep(2000)
