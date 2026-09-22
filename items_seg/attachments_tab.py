import time
from entry_docs import COMMERCIAL_INVOICE, CERTIFICATE_OF_ORIGIN
from utils import manual_type
from playwright.sync_api import Page

def attachments_tab(page:Page):
    iframe = page.locator("#form-tabs-iframeArea").frame_locator("iframe").last
    tab = iframe.locator(".tabs-back-div").locator("div[title=Attachments]")
    tab.click()
    
    commercial_invoice = {
        "file_path": "commercial_invoice.pdf",
        "ref": "210",
        "serial_number": COMMERCIAL_INVOICE.serial_number
    }

    packing_list = {
        "file_path": "packing_list.pdf",
        "ref": "220",
        "serial_number": COMMERCIAL_INVOICE.serial_number
    }

    certificate_of_origin = {
        "file_path": "certificate_of_origin.pdf",
        "ref": "53",
        "serial_number": CERTIFICATE_OF_ORIGIN.serial_number
    }

    attachments = [commercial_invoice, packing_list, certificate_of_origin]

    for attachment in attachments:
        add_attachment_btn = iframe.locator("#Tbl7510V2TableAddDelCol").locator("a")
        add_attachment_btn.click()

        row = iframe.locator("#Tbl7510").locator(".DATACONTAINER").locator(".row").last

        row.click()

        certificate_type_input = iframe.locator("#List9030").locator("input").first
        manual_type(page, certificate_type_input, "A")
        time.sleep(1)

        certificate_ref_input = iframe.locator("#List9032").locator("input").first
        manual_type(page, certificate_ref_input, attachment["ref"])
        time.sleep(1)

        certificate_serial_num_input = iframe.locator("#Field11411").locator("input").first
        certificate_serial_num_input.fill(attachment["serial_number"])

        upload_btn = iframe.locator("#selectOneFile").locator("input").first
        upload_btn.click()


        box_iframe = iframe.frame_locator(".fancybox-iframe")
        print("file inputs: ", box_iframe.locator('input[type="file"]').count())
        select_file_input = box_iframe.locator("#uploadBt").locator("input").first
        upload = select_file_input

        with page.expect_file_chooser() as fc_info:
            upload.click()


        file_chooser = fc_info.value
        file_chooser.set_files(f"attachments/{attachment["file_path"]}")

        time.sleep(2)

        submit_btn = box_iframe.locator("#tbContainer").locator("#tbSubmit").locator("input").first
        submit_btn.click()
        submit_btn.wait_for(state="detached")





