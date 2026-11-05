from fastapi import APIRouter
import sqlite3

router = APIRouter(prefix="/veg", tags=["vegetables"])

@router.get("/")
def get_vegetables():
    return {"items": ["Carrot", "Broccoli", "Spinach"]}
