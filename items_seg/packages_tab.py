from utils import LpDetails, manual_type
from playwright.sync_api import Page
from entry_docs import PACKING_LIST

def packages_tab(page: Page, line_item_index: int, lp_details: LpDetails):
    iframe = page.locator("#form-tabs-iframeArea").frame_locator("iframe").last
    tab = iframe.locator(".tabs-back-div").locator("div[title=Packages]")
    tab.click()
    if line_item_index > 0:
        add_pkg_btn = iframe.locator("#Tbl7508V2TableAddDelCol").locator("a")
        add_pkg_btn.click()
    row = iframe.locator(".DATACONTAINER").locator(".row").last
    row.click()
    type_package_input = iframe.locator("#sclist1058").locator("input").first
    manual_type(page, type_package_input, PACKING_LIST.line_items[line_item_index].package.code)
    declared_qty_input = iframe.locator("#Field11043").locator("input")
    declared_qty_input.fill(PACKING_LIST.line_items[line_item_index].package.qty)
    marks_input = iframe.locator("#Field11044").locator("input")
    marks_description = f"1 x {lp_details.container_ref}"
    marks_input.fill(marks_description)
    gross_mass_input = iframe.locator("#Field11045").locator("input")
    gross_mass_input.fill(PACKING_LIST.line_items[line_item_index].total_gross_mass)
    description_input = iframe.locator("#Field11046").locator("input")
    description_input.fill(PACKING_LIST.line_items[line_item_index].name)
    unique_lp_ref_input = iframe.locator("#Unique_LP").locator("input")
    unique_lp_ref_input.fill(lp_details.unique_lp_no)

    
