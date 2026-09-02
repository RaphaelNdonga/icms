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
    country: str | None = None
    country_code: str | None = None


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


def get_commercial_invoice():
    return Commercial_Invoice(**entry_docs["commercial_invoice"])


def get_insurance():
    return Insurance(**entry_docs["insurance"])


def get_bill_of_lading():
    return BillOfLading(**entry_docs["bill_of_lading"])


def get_certificate_of_origin():
    certificate_data = entry_docs["certificate_of_origin"]
    return CertificateOfOrigin(
        consignor=Party(**certificate_data["consignor"]),
        consignee=Party(**certificate_data["consignee"]),
    )


def get_import_declaration_form():
    declaration_data = entry_docs["import_declaration_form"]
    return ImportDeclarationForm(
        no=declaration_data["no"],
        pin=declaration_data["pin"],
        importer=Importer(**declaration_data["importer"]),
        seller=Seller(**declaration_data["seller"]),
        mode_of_transport=declaration_data["mode_of_transport"],
    )