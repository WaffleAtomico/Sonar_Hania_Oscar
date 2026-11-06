from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import sqlite3
from database import get_db_connection, create_product, get_products_by_category, update_product, delete_product

router = APIRouter(prefix="/vegetable", tags=["vegetables"])

class Product(BaseModel):
    name: str
    price: float

@router.get("/")
def get_vegetables():
    return {"items": get_products_by_category('Vegetable')}

@router.post("/")
def add_veg(product: Product):
    new_id = create_product(product.name, 'Vegetable', product.price)
    return {"id": new_id, "message": "Vegetable added"}

@router.put("/{product_id}")
def update_veg(product_id: int, product: Product):
    update_product(product_id, product.name, product.price)
    return {"message": "Vegetable updated"}

@router.delete("/{product_id}")
def delete_veg(product_id: int):
    delete_product(product_id)
    return {"message": "Vegetable deleted"}
