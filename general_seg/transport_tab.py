import time
from utils import LpDetails, manual_type, manual_del, gradual_top_bottom_scroll
from playwright.sync_api import Page, Locator
from entry_docs import BILL_OF_LADING

def transport_tab(page:Page, settled = False):
    iframe = page.locator("#form-tabs-iframeArea").frame_locator("iframe").last
    tab = iframe.locator(".tabs-back-div").locator("div[title=Transport]")
    tab.click()

    manifest_number = fetch_manifest()

    if not settled:
        bill_search = iframe.locator("#billSearch").locator("input")
        bill_search.fill(BILL_OF_LADING.no)

        summary_decl_num = iframe.locator("#Field12431").locator("input").first
        summary_decl_num.fill(manifest_number)

        search_tdid_btn = iframe.locator("#But8511")
        search_tdid_btn.click()

    summary_decl_page_btn = iframe.locator("#Field12431-Link_Button")
    summary_decl_page_btn.click()
    list_lp_details = fetch_summary_decl_info(iframe)
    return list_lp_details
    

def fetch_summary_decl_info(iframe:Locator) -> list[LpDetails]:
    lp_table = iframe.locator("#Tbl5")
    lp_table.wait_for(state="visible", timeout=60000)
    lp_table.click()

    visual_data_container = lp_table.locator(".VISUAL_DATACONTAINER")
    gradual_top_bottom_scroll(visual_data_container) 

    row = visual_data_container.locator(".row")

    row.nth(0).click()

    list_lp_details = []

    for i in range(row.count()):
        current_row = row.nth(i)
        current_row.click()
        print("Current row: ", current_row)
        uniq_lp_ref = current_row.locator("td").nth(1).locator(".refdiv").text_content()
        description_goods = current_row.locator("td").nth(4).locator(".refdiv").text_content()
        declared_qty = current_row.locator("td").nth(5).locator(".refdiv").text_content()
        gross_wt = current_row.locator("td").nth(6).locator(".refdiv").text_content()
        actual_qty = current_row.locator("td").nth(7).locator(".refdiv").text_content()
        actual_wt = current_row.locator("td").nth(8).locator(".refdiv").text_content()

        lp_details = LpDetails(
            number=str(i + 1),
            uniq_lp_ref=uniq_lp_ref,
            description_goods=description_goods,
            declared_qty=declared_qty,
            gross_wt=gross_wt,
            actual_qty=actual_qty,
            actual_wt = actual_wt,
            container_no=""
        )


        display_lp_btn = iframe.locator("#But417")
        display_lp_btn.click()
        fancy_box_opened = iframe.locator(".fancybox-opened")
        fancy_box_opened.wait_for(state="attached")

        modal_iframe = iframe.frame_locator(".fancybox-iframe")
        lp_details = fetch_lp_details(modal_iframe, lp_details)
        list_lp_details.append(lp_details)
        close_btn = iframe.locator(".fancybox-close")
        close_btn.click()
        close_btn.wait_for(state="hidden")
        row.nth(0).click()

    return list_lp_details


def fetch_lp_details(modal_iframe: Locator, lp_details: LpDetails):
    container_ref = modal_iframe.locator("#KRA_Field_container_reference_id").locator("input").input_value()
    lp_details.container_no = container_ref

    return lp_details


def fetch_manifest() -> str:
    return "2026MSASI0124333"