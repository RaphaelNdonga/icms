import json
from dataclasses import dataclass

entry_docs = {}

with open("entry_items.json", "r") as file:
    entry_items = json.load(file)


@dataclass
class EntryPackage:
    code: str
    qty: str
    description: str
    marks: str
    uniq_lp: str
    lp_actual_wt: str


@dataclass
class EntryItem:
    number: str
    idf_item_number: str
    idf_item_description: str
    total_gross_mass: str
    idf_net_mass: str
    total_qty: str
    idf_qty: str
    unit_fob: str
    total_fob: str
    packages: list[EntryPackage]
    generation_remarks: str | None = None

@dataclass
class EntryItems:
    entry_items: list[EntryItem]

_entry_items_data = entry_items["items"]

ENTRY_ITEMS = EntryItems(
    entry_items=[
        EntryItem(
            **{
                **entry_item,
                "packages": [
                    EntryPackage(**entry_pkg)
                    for entry_pkg in entry_item["packages"]
                ],
            }
        )
        for entry_item in _entry_items_data
    ]
)
