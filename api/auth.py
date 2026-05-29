
import base64
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials

USERNAME = "admin"
PASSWORD = "password123"


def check_auth(header):

    if not header:
        return False

    try:

        auth_type, credentials = header.split()

        if auth_type != "Basic":
            return False

        decoded = base64.b64decode(credentials).decode()

        username, password = decoded.split(":")

        return (
            username == USERNAME
            and password == PASSWORD
        )

    except Exception:
        return False