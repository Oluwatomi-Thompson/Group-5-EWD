
transactions = []
next_id = 1

import sqlite3

def get_connection():
    conn = sqlite3.connect("sms.db")  # or your actual DB file
    return conn

def get_all():
    return transactions


def get_by_id(transaction_id):
    for t in transactions:
        if t["id"] == transaction_id:
            return t
    return None


def insert(transaction):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO sms (address, body, date, type, category)
    VALUES (?, ?, ?, ?, ?)
    """, (
        transaction["address"],
        transaction["body"],
        transaction["date"],
        transaction["type"],
        transaction["category"]
    ))

    conn.commit()
    conn.close()
    return transaction


def update(transaction_id, data):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE sms
    SET address = ?, body = ?, date = ?, type = ?, category = ?
    WHERE id = ?
    """, (
        data["address"],
        data["body"],
        data["date"],
        data["type"],
        data["category"],
        transaction_id
    ))

    conn.commit()
    conn.close()
    return transaction


def delete(transaction_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM sms WHERE id = ?", (transaction_id,))
    conn.commit()
    conn.close()
    return True