from fastapi import APIRouter
from typing import Dict, List
from app.controllers.item_controller import ItemController
from app.schemas.item import Item

router = APIRouter()
controller = ItemController()

@router.get("/", response_model=Dict[str, str])
async def root():
    return controller.get_welcome_message()

@router.get("/items", response_model=List[Item])
async def get_items():
    return controller.get_items()
    
@router.get("/items/{item_id}", response_model=Item)
async def get_item_by_id(item_id: int):
    return controller.get_item_by_id(item_id)
