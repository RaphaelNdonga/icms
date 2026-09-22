import json
from dataclasses import dataclass

entry_docs = {}

with open("entry_docs.json", "r") as file:
    entry_docs = json.load(file)

@dataclass
class Line_Item_CI:
    number: str
    name: str
    qty: str
    unit_price: str
    total_price: str


@dataclass
class Commercial_Invoice:
    incoterms: str
    currency: str
    fob_amount: str
    freight_amount: str
    line_items: list[Line_Item_CI]

@dataclass
class Package:
    type: str
    code: str
    qty: str

@dataclass
class Line_Item_PL:
    number: str
    name: str
    qty: str
    package: Package
    total_gross_mass: str
    total_net_mass: str


@dataclass
class PackingList:
    line_items: list[Line_Item_PL]

@dataclass
class Insurance:
    currency: str
    amount: str


@dataclass
class BillOfLading:
    no: str
    place_of_delivery: str


@dataclass
class Party:
    name: str
    address: str
    country: str
    country_code: str 


@dataclass
class CertificateOfOrigin:
    consignor: Party
    consignee: Party


@dataclass
class Importer:
    name: str
    address: str
    county_code: str


@dataclass
class Seller:
    name: str
    address: str

@dataclass
class ModeOfTransport:
    name: str
    code: str

@dataclass
class ImportDeclarationForm:
    no: str
    pin: str
    importer: Importer
    seller: Seller
    mode_of_transport: ModeOfTransport

_commercial_invoice_data = entry_docs["commercial_invoice"]
COMMERCIAL_INVOICE = Commercial_Invoice(
    incoterms=_commercial_invoice_data["incoterms"],
    currency=_commercial_invoice_data["currency"],
    fob_amount=_commercial_invoice_data["fob_amount"],
    freight_amount=_commercial_invoice_data["freight_amount"],
    line_items=[Line_Item_CI(**line_item) for line_item in _commercial_invoice_data["line_items"]],
)

_packing_list_data = entry_docs["packing_list"]
PACKING_LIST = PackingList(
    line_items=[
        Line_Item_PL(
            **{
                **line_item,
                "package": Package(**line_item["package"]),
            }
        )
        for line_item in _packing_list_data["line_items"]
    ]
)


INSURANCE = Insurance(**entry_docs["insurance"])


BILL_OF_LADING = BillOfLading(**entry_docs["bill_of_lading"])


_certificate_data = entry_docs["certificate_of_origin"]

CERTIFICATE_OF_ORIGIN = CertificateOfOrigin(
        consignor=Party(**_certificate_data["consignor"]),
        consignee=Party(**_certificate_data["consignee"]),
    )

_declaration_data = entry_docs["import_declaration_form"]
IMPORT_DECLARATION_FORM = ImportDeclarationForm(
        no=_declaration_data["no"],
        pin=_declaration_data["pin"],
        importer=Importer(**_declaration_data["importer"]),
        seller=Seller(**_declaration_data["seller"]),
        mode_of_transport=ModeOfTransport(**_declaration_data["mode_of_transport"]),
    )