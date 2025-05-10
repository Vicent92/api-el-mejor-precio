from typing import List
from app.schemas.item import Item

class ItemController:
    @staticmethod
    def get_items() -> List[Item]:
        # Simulando datos de una base de datos
        items = [
            Item(id=1, name="Producto 1", price=100),
            Item(id=2, name="Producto 2", price=200)
        ]
        return items

    @staticmethod
    def get_welcome_message() -> dict:
        return {"message": "Bienvenido a la API El Mejor Precio"}
