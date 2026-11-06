from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import sqlite3
from database import get_db_connection, create_product, get_products_by_category, update_product, delete_product

router = APIRouter(prefix="/fruit", tags=["fruits"])

class Product(BaseModel):
    name: str
    price: float

@router.get("/")
def get_fruits():
    return {"items": get_products_by_category('Fruit')}

@router.post("/")
def add_fruit(product: Product):
    new_id = create_product(product.name, 'Fruit', product.price)
    return {"id": new_id, "message": "Fruit added"}

@router.put("/{product_id}")
def update_fruit(product_id: int, product: Product):
    update_product(product_id, product.name, product.price)
    return {"message": "Fruit updated"}

@router.delete("/{product_id}")
def delete_fruit(product_id: int):
    delete_product(product_id)
    return {"message": "Fruit deleted"}
