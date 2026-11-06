from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import sqlite3
from database import get_db_connection, create_product, get_products_by_category, update_product, delete_product

router = APIRouter(prefix="/dairy", tags=["dairy"])

class Product(BaseModel):
    name: str
    price: float

@router.get("/")
def get_dairy():
    return {"items": get_products_by_category('Dairy')}

@router.post("/")
def add_dairy(product: Product):
    new_id = create_product(product.name, 'Dairy', product.price)
    return {"id": new_id, "message": "Dairy added"}

@router.put("/{product_id}")
def update_dairy(product_id: int, product: Product):
    update_product(product_id, product.name, product.price)
    return {"message": "Dairy updated"}

@router.delete("/{product_id}")
def delete_dairy(product_id: int):
    delete_product(product_id)
    return {"message": "Dairy deleted"}
