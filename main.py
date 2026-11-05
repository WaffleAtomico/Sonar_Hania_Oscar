import sqlite3
from fastapi import FastAPI
from fruits import router as fruits_router
from veg import router as veg_router
from meat import router as meat_router
from dairy import router as dairy_router

app = FastAPI()

def get_db_connection():
    # Placeholder for SQLite connection
    conn = sqlite3.connect('market.db')
    return conn

app.include_router(fruits_router)
app.include_router(veg_router)
app.include_router(meat_router)
app.include_router(dairy_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Market Shop"}
