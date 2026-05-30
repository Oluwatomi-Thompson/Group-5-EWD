
from http.server import BaseHTTPRequestHandler, HTTPServer
import json, base64

from api.db import *
from api import USERNAME, PASSWORD
from api.schemas import validate_transaction


class Handler(BaseHTTPRequestHandler):

    def auth(self):
        h = self.headers.get("Authorization")
        if not h:
            return False

        try:
            _, cred = h.split()
            u, p = base64.b64decode(cred).decode().split(":")
            return u == USERNAME and p == PASSWORD
        except:
            return False

    def send(self, data, code=200):
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_GET(self):
        if not self.auth():
            return self.send({"error": "Unauthorized"}, 401)

        if self.path == "/transactions":
            return self.send(get_all())

        tid = int(self.path.split("/")[-1])
        return self.send(get_by_id(tid) or {"error": "Not found"})

    def do_POST(self):
        if not self.auth():
            return self.send({"error": "Unauthorized"}, 401)

        data = json.loads(
            self.rfile.read(
                int(self.headers["Content-Length"])
            )
        )

        valid, message = validate_transaction(data)

        if not valid:
            return self.send(
                {"error": message},
                400
            )

        transaction = insert(data)

        return self.send(
            transaction,
            201
        )

    def do_PUT(self):
        if not self.auth():
            return self.send({"error": "Unauthorized"}, 401)

        tid = int(self.path.split("/")[-1])

        data = json.loads(
            self.rfile.read(
                int(self.headers["Content-Length"])
            )
        )

        valid, message = validate_transaction(data)

        if not valid:
            return self.send(
                {"error": message},
                400
            )

        updated = update(tid, data)

        if not updated:
            return self.send(
                {"error": "Transaction not found"},
                404
            )

        return self.send(updated)
    def do_DELETE(self):
        if not self.auth():
            return self.send({"error": "Unauthorized"}, 401)

        tid = int(self.path.split("/")[-1])
        return self.send({"deleted": delete(tid)})


HTTPServer(("localhost", 8000), Handler).serve_forever()