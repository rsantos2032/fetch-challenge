class Item:
    def __init__(self, short_description: str="", price: str = ""):
        self._short_description: str = short_description
        self._price: str = price
        
    def get_short_description(self) -> str:
        return self._short_description
    
    def set_short_description(self, short_description: str) -> None:
        self._short_description = short_description
    
    def get_price(self) -> str:
        return self._price
    
    def set_price(self, price: str):
        self._price = price        