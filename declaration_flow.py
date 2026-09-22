import time
from utils import launch_browser, icms_sign_in, LpDetails
from search_entry import search_entry
from general_seg.details_tab import details_tab
from general_seg.movements_tab import movements_tab
from general_seg.transport_tab import transport_tab
from items_seg.details_tab import item_details_tab
from items_seg.packages_tab import packages_tab
from items_seg.attachments_tab import attachments_tab

browser = launch_browser()
page = icms_sign_in(browser)

search_entry(page, "26EMKIM401078120")
# search_entry(page, "26EMKIM401055916", settled = True)
details_tab(page)
movements_tab(page)

iframe = page.locator("#form-tabs-iframeArea").frame_locator("iframe").last

items_radio = iframe.locator("#Field8462").locator("input")
items_radio.click()

item_details_tab(page, 0)


# list_lp_details = transport_tab(page, settled=True)
# for lp in list_lp_details:
#     print(lp)
#     print("\n")

lp_details = LpDetails(
    unique_lp_no='2',
    type_of_pkg='CT', 
    declared_qty='456.000', 
    gross_wt='13,008.000', 
    comdty_code='9403500000', 
    mrks_pkgs='N/M', 
    desc_goods="2 X 40'HQ  CONTAINERS STC:-,932 CARTONS OF BEDROOM  ,FURNITURE,H.S.CODE 9403.50.0000,,,PLACE OF DELIVERY ICDE,", 
    un_dangerous='', 
    country_origin='MY', 
    net_wt='13,008.000', 
    temp='', 
    volume='63.000', 
    volume_unit='M3', 
    container_ref='CSNU6373526', 
    remarks=''
    )

packages_tab(page, 0, lp_details)

attachments_tab(page)

time.sleep(20)
