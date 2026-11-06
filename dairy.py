from fastapi import APIRouter
import sqlite3
from database import get_db_connection

router = APIRouter(prefix="/dairy", tags=["dairy"])

@router.get("/")
def get_dairy():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE category='Dairy'")
    rows = cursor.fetchall()
    conn.close()
    return {"items": [dict(row) for row in rows]}
