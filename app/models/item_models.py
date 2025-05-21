from typing import List, Optional
from app.schemas.item import Item

data = [
    Item(id=1, name="Producto 1", price=100),
    Item(id=2, name="Producto 2", price=200)
]
class ItemModel:
    @staticmethod
    def get_items() -> List[Item]:
        items = data
        
        return items
        
    @staticmethod
    def get_item_by_id(item_id: int) -> Optional[Item]:
        
        for item in data:
            if item.id == item_id:
                return item
                
        return None
        