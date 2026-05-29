from fastapi import Body
from fastapi import FastAPI, Request
from api.db import get_connection
from etl.load_db import fetch_all_sms
import sqlite3
from etl.load_db import DB_PATH

app = FastAPI(title="SMS ETL System")

# -------------------------
# HOME
# -------------------------
@app.get("/")
def home():
    return {"message": "SMS ETL API is running"}

# -------------------------
# GET ALL SMS
# -------------------------
@app.get("/sms")
def get_sms():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM sms LIMIT 50")
    rows = cursor.fetchall()

    return {
        "count": len(rows),
        "data": rows
    }

# -------------------------
# COUNT SMS
# -------------------------
@app.get("/sms/count")

def count_sms():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM sms")
    total = cursor.fetchone()[0]

    return {"total_sms": total}

# -------------------------
# SEARCH SMS
# -------------------------
@app.get("/sms/search/{keyword}")
def search_sms(keyword: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM sms WHERE body LIKE ? LIMIT 20",
        ('%' + keyword + '%',)
    )

    rows = cursor.fetchall()

    return {
        "count": len(rows),
        "results": rows
    }


@app.post("/transactions")

def create_transaction(date: dict = Body(...)):
    data = date

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO sms (address, body, date, type, category)
        VALUES (?, ?, ?, ?, ?)
    """, (
        data["address"],
        data["body"],
        data["date"],
        data["type"],
        data["category"]
    ))

    conn.commit()
    conn.close()

    return {"message": "Transaction created successfully"}

@app.delete("/transactions/{id}")
def delete_transaction(id: int):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM sms WHERE id = ?", (id,))

    conn.commit()
    conn.close()

    return {"message": f"Transaction {id} deleted successfully"}