import time
from utils import manual_type, manual_del
from playwright.sync_api import Page
import json
from entry_docs import COMMERCIAL_INVOICE, BILL_OF_LADING, IMPORT_DECLARATION_FORM, CERTIFICATE_OF_ORIGIN, INSURANCE

def details_tab(page:Page):
    iframe = page.locator("#form-tabs-iframeArea").frame_locator("iframe").last
    tab = iframe.locator(".tabs-back-div").locator("div[title=Details]")
    tab.click()
    incoterm_code_input = iframe.locator("#sclist1099").locator("input").first
    manual_del(incoterm_code_input)
    manual_type(page, incoterm_code_input, COMMERCIAL_INVOICE.incoterms)

    named_place_input = iframe.locator("#Field8947").locator("input").first
    named_place_input.fill(BILL_OF_LADING.place_of_delivery)

    fob_amount_input = iframe.locator("#Field8966").locator("input")
    fob_amount_input.fill(COMMERCIAL_INVOICE.fob_amount)

    fob_currency_input = iframe.locator("#sclist8006").locator("input").first
    manual_del(fob_currency_input)
    manual_type(page, fob_currency_input, COMMERCIAL_INVOICE.currency)

    consignee_reg_number_input = iframe.locator("#Field11257").locator("input")
    consignee_reg_number_input.fill(IMPORT_DECLARATION_FORM.pin)

    freight_invoiced_input = iframe.locator("#FieldFreightInvoiced").locator("input")
    freight_invoiced_input.fill(COMMERCIAL_INVOICE.freight_amount)

    insurance_invoiced_input = iframe.locator("#FieldInsuranceInvoiced").locator("input")
    insurance_invoiced_input.fill(INSURANCE.amount)

    time.sleep(1)

    insurance_currency_input = iframe.locator("#sclistInsuranceInvoiced").locator("input").first
    manual_del(insurance_currency_input)
    manual_type(page, insurance_currency_input, INSURANCE.currency)

    time.sleep(1)

    freight_currency_input = iframe.locator("#sclistFreightInvoiced").locator("input").first
    manual_del(freight_currency_input)
    manual_type(page, freight_currency_input, COMMERCIAL_INVOICE.currency)

    # valuation_method_input = iframe.locator("#b12_valuation_method").locator("input").first
    # manual_del(valuation_method_input)
    # manual_type(page, valuation_method_input, "1")

    consignor_name_input = iframe.locator("#Field8465").locator("input")
    consignor_name_input.fill(CERTIFICATE_OF_ORIGIN.consignor.name)

    consignor_address_input = iframe.locator("#Field8466").locator("textarea")
    consignor_address_input.fill(CERTIFICATE_OF_ORIGIN.consignor.address)

    consignor_nation_input = iframe.locator("#sclist8000").locator("input").first
    manual_del(consignor_nation_input)
    manual_type(page, consignor_nation_input, CERTIFICATE_OF_ORIGIN.consignor.country_code)

