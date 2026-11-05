from fastapi import APIRouter
import sqlite3

router = APIRouter(prefix="/fruits", tags=["fruits"])

@router.get("/")
def get_fruits():
    return {"items": ["Apple", "Banana", "Orange"]}
