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

def get_commercial_invoice():
    return Commercial_Invoice(**entry_docs["commercial_invoice"])