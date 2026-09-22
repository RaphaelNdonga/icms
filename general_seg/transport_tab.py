import time
from utils import LpDetails, manual_type, manual_del
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

    summary_decl_page_btn = iframe.locator("#Field12431-Link_Button")
    summary_decl_page_btn.click()
    list_lp_details = fetch_summary_decl_info(iframe)
    return list_lp_details
    

def fetch_summary_decl_info(iframe:Locator) -> list[LpDetails]:
    lp_table = iframe.locator("#Tbl5")
    lp_table.wait_for(state="visible", timeout=60000)
    lp_table.click()

    visual_data_container = lp_table.locator(".VISUAL_DATACONTAINER")
    visual_data_container.evaluate("(el) => el.scrollTop = el.scrollHeight")

    row = visual_data_container.locator(".row")

    row.nth(0).click()

    list_lp_details = []

    for i in range(row.count()):
        current_row = row.nth(i)
        current_row.click()
        print("Current row: ", current_row)
        display_lp_btn = iframe.locator("#But417")
        display_lp_btn.click()
        fancy_box_opened = iframe.locator(".fancybox-opened")
        fancy_box_opened.wait_for(state="attached")

        modal_iframe = iframe.frame_locator(".fancybox-iframe")
        lp_details = fetch_lp_details(modal_iframe)
        list_lp_details.append(lp_details)
        close_btn = iframe.locator(".fancybox-close")
        close_btn.click()
        close_btn.wait_for(state="hidden")
        row.nth(0).click()
        


    return list_lp_details


def fetch_lp_details(modal_iframe: Locator):
    unique_lp_no = modal_iframe.locator("#Field235").locator("input").input_value()
    type_of_pkg = modal_iframe.locator("#sclist60").locator("input").first.input_value()
    declared_qty = modal_iframe.locator("#Field96").locator("input").input_value()
    gross_wt = modal_iframe.locator("#Field97").locator("input").input_value()
    comdty_code = modal_iframe.locator("#Field236").locator("input").input_value()
    mrks_pkgs = modal_iframe.locator("#Field98").locator("textarea").input_value()
    desc_goods = modal_iframe.locator("#Field101").locator("textarea").input_value()
    un_dangerous = modal_iframe.locator("#List237").locator("input").first.input_value()
    country_origin = modal_iframe.locator("#KRA_Field_origin_country_id").locator("input").first.input_value()
    net_wt = modal_iframe.locator("#KRA_Field_net_weight_status_id").locator("input").input_value()
    temp = modal_iframe.locator("#KRA_Field_temperature_id").locator("input").input_value()
    volume = modal_iframe.locator("#KRA_Field_volume_id").locator("input").input_value()
    volume_unit = modal_iframe.locator("#List238").locator("input").first.input_value()
    container_ref = modal_iframe.locator("#KRA_Field_container_reference_id").locator("input").input_value()
    remarks = modal_iframe.locator("#KRA_Field_remarks").locator("textarea").input_value()

    return LpDetails(
        unique_lp_no=unique_lp_no,
        type_of_pkg=type_of_pkg,
        declared_qty=declared_qty,
        gross_wt=gross_wt,
        comdty_code=comdty_code,
        mrks_pkgs=mrks_pkgs,
        desc_goods=desc_goods,
        un_dangerous=un_dangerous,
        country_origin=country_origin,
        net_wt=net_wt,
        temp=temp,
        volume=volume,
        volume_unit=volume_unit,
        container_ref=container_ref,
        remarks=remarks,
    )


def fetch_manifest() -> str:
    return "2026MSASI0111717"