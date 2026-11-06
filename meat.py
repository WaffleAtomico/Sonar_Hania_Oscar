from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import sqlite3
from database import get_db_connection, create_product, get_products_by_category, update_product, delete_product

router = APIRouter(prefix="/meat", tags=["meat"])

class Product(BaseModel):
    name: str
    price: float

@router.get("/")
def get_meat():
    return {"items": get_products_by_category('Meat')}

@router.post("/")
def add_meat(product: Product):
    new_id = create_product(product.name, 'Meat', product.price)
    return {"id": new_id, "message": "Meat added"}

@router.put("/{product_id}")
def update_meat(product_id: int, product: Product):
    update_product(product_id, product.name, product.price)
    return {"message": "Meat updated"}

@router.delete("/{product_id}")
def delete_meat(product_id: int):
    delete_product(product_id)
    return {"message": "Meat deleted"}
