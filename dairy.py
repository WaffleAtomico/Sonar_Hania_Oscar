from fastapi import APIRouter
import sqlite3

router = APIRouter(prefix="/dairy", tags=["dairy"])

@router.get("/")
def get_dairy():
    return {"items": ["Milk", "Cheese", "Yogurt"]}
