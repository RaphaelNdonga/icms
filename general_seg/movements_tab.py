import time
from utils import manual_type, manual_del
from playwright.sync_api import Page
from entry_docs import IMPORT_DECLARATION_FORM, CERTIFICATE_OF_ORIGIN

def movements_tab(page:Page):
    iframe = page.locator("#form-tabs-iframeArea").frame_locator("iframe").last
    tab = iframe.locator(".tabs-back-div").locator("div[title=Movements]")
    tab.click()

    country_last_consignment = iframe.locator("#sclist8003").locator("input").first
    manual_del(country_last_consignment)
    manual_type(page, country_last_consignment, CERTIFICATE_OF_ORIGIN.consignor.country_code)
    time.sleep(1)

    region_destination = iframe.locator("#region_of_destination_code").locator("input").first
    manual_del(region_destination)
    manual_type(page, region_destination, IMPORT_DECLARATION_FORM.importer.county_code)
    time.sleep(1)

    mode_of_trans = iframe.locator("#sclist1052").locator("input").first
    manual_del(mode_of_trans)
    manual_type(page, mode_of_trans, IMPORT_DECLARATION_FORM.mode_of_transport.code)
    time.sleep(1)

    place_of_unloading_country = iframe.locator("#countrySDS").locator("input").first
    manual_del(place_of_unloading_country)
    manual_type(page, place_of_unloading_country, CERTIFICATE_OF_ORIGIN.consignor.country_code)

    time.sleep(1)

    place_of_unloading_region = iframe.locator("#box27Place").locator("input").first
    manual_del(place_of_unloading_region)
    manual_type(page, place_of_unloading_region, CERTIFICATE_OF_ORIGIN.consignor.country_code)
    page.keyboard.press("Enter")


