Read all pages of the three attached scanned PDFs visually. Extract the commercial_invoice, packing_list, and certificate_of_origin objects using the field names and structure below. Return only one valid JSON object, with no Markdown or explanation.

Rules:
- Include every product row in both line_items arrays, in document order. Do not treat collection headings or totals as product rows.
- Number product rows sequentially as strings: "1", "2", and so on. For each name, combine its collection or brand name with its product description.
- Keep all scalar values as strings. Remove thousands separators and unnecessary trailing ".00" from numbers.
- On the packing list, qty means units; package.qty means cartons. Use the row's total gross and total net weights, not unit weights. Map “Cartons” to package type "Carton" and code "CT".
- Format the container count and size like the example in entry_docs.json: “2 X 40'HQ” becomes "2x40".
- For the certificate, use the reference number as serial_number. Put each party’s full printed address on one line, and use two-letter country codes.
- Use an empty string for a field that is absent or unreadable. Never copy a value from the example JSON merely to fill a gap. In particular, do not treat “other charges” as freight or infer an Incoterm from an F.O.B. value.
- Do not add insurance, bill_of_lading, or import_declaration_form objects; their source documents are not attached.

Output structure (replace the empty values and repeat line-item objects for every product row):

{
  "commercial_invoice": {
    "incoterms": "",
    "currency": "",
    "fob_amount": "",
    "freight_amount": "",
    "line_items": [
      {
        "number": "",
        "name": "",
        "qty": "",
        "unit_price": "",
        "total_price": ""
      }
    ],
    "serial_number": ""
  },
  "packing_list": {
    "line_items": [
      {
        "number": "",
        "name": "",
        "qty": "",
        "package": {
          "type": "",
          "code": "",
          "qty": ""
        },
        "total_gross_mass": "",
        "total_net_mass": ""
      }
    ],
    "total_containers_x_size": []
  },
  "certificate_of_origin": {
    "serial_number": "",
    "consignor": {
      "name": "",
      "address": "",
      "country": "",
      "country_code": ""
    },
    "consignee": {
      "name": "",
      "address": "",
      "country": "",
      "country_code": ""
    }
  }
}