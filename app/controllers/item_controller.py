from typing import List
from app.schemas.item import Item
from app.models.item_models import ItemModel

class ItemController:
    @staticmethod
    def get_items() -> List[Item]:
        # Simulando datos de una base de datos
        items = ItemModel.get_items()
        
        return items
        
    @staticmethod
    def get_item_by_id(item_id: int) -> Item:
        item = ItemModel.get_item_by_id(item_id)
        
        if item == None:
            return 404
        
        return item
        
    @staticmethod
    def get_welcome_message() -> dict:
        return {"message": "Bienvenido a la API El Mejor Precio"}
