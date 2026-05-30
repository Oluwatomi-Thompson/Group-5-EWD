
import sqlite3

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "sms.db")


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sms (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        address TEXT,
        body TEXT,
        date TEXT,
        type TEXT,
        category TEXT
    )
    """)

    conn.commit()
    conn.close()


def insert_sms(sms_list):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for sms in sms_list:
        cursor.execute("""
        INSERT INTO sms (address, body, date, type, category)
        VALUES (?, ?, ?, ?, ?)
        """, (
            sms["address"],
            sms["body"],
            sms["date"],
            sms["type"],
            sms["category"]
        ))

    conn.commit()
    conn.close()


def fetch_all_sms():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM sms")
    rows = cursor.fetchall()

    conn.close()

    return [
        {
            "id": row[0],
            "address": row[1],
            "body": row[2],
            "date": row[3],
            "type": row[4],
            "category": row[5]
        }
        for row in rows
    ]
    