

""" dataclasses """
from dataclasses import dataclass

@dataclass
class InventoryItem:
    name: str
    unit_price: float
    quantity_on_hand: int = 0
    
    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand
    
i = InventoryItem("miecz", 23.0, 2)

print(i.total_cost())
    

