from generation_models import ENTRY_ITEMS
from playwright.sync_api import Page

def item_details_tab(page:Page, line_item_index: int):
    iframe = page.locator("#form-tabs-iframeArea").frame_locator("iframe").last
    tab = iframe.locator(".tabs-back-div").locator("div[title=Details]")
    tab.click()
    gross_mass_input = iframe.locator("#Field11034").locator("input")
    gross_mass_input.click()
    gross_mass_input.fill(ENTRY_ITEMS.entry_items[line_item_index].total_gross_mass)
    net_mass_input = iframe.locator("#Field11035").locator("input")
    net_mass_input.fill(ENTRY_ITEMS.entry_items[line_item_index].idf_net_mass)
    num_units_input = iframe.locator("#Field12616").locator("input")
    num_units_input.fill(ENTRY_ITEMS.entry_items[line_item_index].total_qty)
    item_price_fob_input = iframe.locator("#Field11213").locator("input")
    item_price_fob_input.fill(ENTRY_ITEMS.entry_items[line_item_index].total_fob)