# Sonar_Hania_Oscar - Market Shop

A simple FastAPI application demonstrating a market shop with different categories of products stored in a SQLite database.

## Features
- FastAPI backend with multiple routers (Fruits, Vegetables, Meat, Dairy).
- SQLite database integration.
- Automatic database population from a CSV file.
- Simple HTML dashboard to view products.

## Setup and Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/WaffleAtomico/Sonar_Hania_Oscar.git
   cd Sonar_Hania_Oscar
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## How to Run

1. **Start the API server**
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the dashboard**
   Open your browser and navigate to:
   `http://127.0.0.1:8000`

## Project Structure
- `main.py`: Entry point and route definitions.
- `database.py`: Database connection and population logic.
- `fruits.py`, `veg.py`, `meat.py`, `dairy.py`: Individual category routers.
- `market_data.csv`: Seed data for the database.
- `frontend.html`: Simple dashboard interface.
