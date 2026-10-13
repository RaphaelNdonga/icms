from utils import manual_type
from playwright.sync_api import Page
from entry_docs import PACKING_LIST
from generation_models import EntryPackage

def packages_tab(page: Page, line_item_index: int, entry_pkg = EntryPackage):
    iframe = page.locator("#form-tabs-iframeArea").frame_locator("iframe").last
    tab = iframe.locator(".tabs-back-div").locator("div[title=Packages]")
    tab.click()
    if line_item_index > 0:
        add_pkg_btn = iframe.locator("#Tbl7508V2TableAddDelCol").locator("a")
        add_pkg_btn.click()
    row = iframe.locator(".DATACONTAINER").locator(".row").last
    row.click()
    type_package_input = iframe.locator("#sclist1058").locator("input").first
    manual_type(page, type_package_input, entry_pkg.code)
    declared_qty_input = iframe.locator("#Field11043").locator("input")
    declared_qty_input.fill(entry_pkg.qty)
    marks_input = iframe.locator("#Field11044").locator("input")
    marks_description = f"1 x {entry_pkg.marks}"
    marks_input.fill(marks_description)
    gross_mass_input = iframe.locator("#Field11045").locator("input")
    gross_mass_input.fill(entry_pkg.lp_actual_wt)
    description_input = iframe.locator("#Field11046").locator("input")
    description_input.fill(entry_pkg.description)
    unique_lp_ref_input = iframe.locator("#Unique_LP").locator("input")
    unique_lp_ref_input.fill(entry_pkg.uniq_lp)

    
