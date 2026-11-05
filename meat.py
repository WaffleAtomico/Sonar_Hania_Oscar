from fastapi import APIRouter
import sqlite3

router = APIRouter(prefix="/meat", tags=["meat"])

@router.get("/")
def get_meat():
    return {"items": ["Beef", "Chicken", "Pork"]}
