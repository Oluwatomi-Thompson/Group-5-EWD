# api/schemes.py

from datetime import date, datetime

REQUIRED_FIELDS = [
    "id",
    "type",
    "amount",
    "sender",
    "receiver",
    "timestamp"
]

def validate_transaction(data):
    """
    Validate incoming transaction payload
     """
     
     # Check required fields
    for field in REQUIRED_FIELDS:
        if field not in data:
            return False, f"Missing required field: {field}"
        
    # Validate amount
    try:
        amount = float(data["amount"])
        if amount <= 0:
            return False, "Amount must be a positive number"
    except ValueError:
        return False, "Amount must be a valid number"
    
    # Validate timestamp
    try:
        datetime.strptime(data["timestamp"], "%Y-%m-%dT%H:%M:%S")
    except ValueError:
        return False, "Timestamp format should be YYYY-MM-DDTHH:MM:SS"

    # Validate sender & receiver
    if not data["sender"].strip():
        return False, "Sender cannot be empty"

    if not data["receiver"].strip():
        return False, "Receiver cannot be empty"
    
    return True, "Valid transaction data"

