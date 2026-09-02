import json
from dataclasses import dataclass

entry_docs = {}

with open("entry_docs.json", "r") as file:
    entry_docs = json.load(file)


@dataclass
class Commercial_Invoice:
    incoterms: str
    currency: str
    fob_amount: str
    freight_amount: str


@dataclass
class Insurance:
    currency: str
    amount: str


@dataclass
class BillOfLading:
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


@dataclass
class Seller:
    name: str
    address: str


@dataclass
class ImportDeclarationForm:
    no: str
    pin: str
    importer: Importer
    seller: Seller
    mode_of_transport: str


COMMERCIAL_INVOICE = Commercial_Invoice(**entry_docs["commercial_invoice"])


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
        mode_of_transport=_declaration_data["mode_of_transport"],
    )