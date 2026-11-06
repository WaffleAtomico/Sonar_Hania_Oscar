import sqlite3
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fruits import router as fruits_router
from veg import router as veg_router
from meat import router as meat_router
from dairy import router as dairy_router
from database import get_db_connection, populate_db

app = FastAPI()

# Populate the DB on startup
@app.on_event("startup")
def startup_event():
    populate_db()

app.include_router(fruits_router)
app.include_router(veg_router)
app.include_router(meat_router)
app.include_router(dairy_router)

@app.get("/api/products")
def get_all_products():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    conn.close()
    return {"products": [dict(row) for row in rows]}

@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("frontend.html", "r") as f:
        return f.read()
