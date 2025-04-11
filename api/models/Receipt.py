from .Item import Item

class Receipt:
    """An object containing all items and total pricing information
    
    Parameters
    ----------
    retailer: `str`
        Store/Business where items were purchased from
    purchase_date: `str`
        Date of purchase of all items
    purchase_time: `str`
        Time of purchase of all items
    items: `list[Item]`
        List of Item objects
    total: `str`
        Total price of all purchased items
    """
    def __init__(self):
        self._retailer: str = ""
        self._purchase_date: str = ""
        self._purchase_time: str = ""
        self._items: list[Item] = []
        self._total: str = ""
        
    def get_retailer(self) -> str:
        return self._retailer

    def set_retailer(self, retailer: str) -> None:
        self._retailer = retailer

    def get_purchase_date(self) -> str:
        return self._purchaseDate

    def set_purchase_date(self, purchase_date: str) -> None:
        self._purchaseDate = purchase_date
        
    def get_purchase_time(self) -> str:
        return self._purchaseTime

    def set_purchase_time(self, purchase_time: str) -> None:
        self._purchaseTime = purchase_time

    def get_items(self) -> list[Item]:
        return self._items

    def set_items(self, items: list[Item]) -> None:
        self._items = items

    def add_item(self, item: Item) -> None:
        self._items.append(item)

    def get_total(self) -> str:
        return self._total

    def set_total(self, total: str) -> None:
        self._total = total