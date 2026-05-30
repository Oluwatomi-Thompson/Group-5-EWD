# tests/test_clean_normalize.py

import unittest
from api.schemas import validate_transaction


class TestTransactionValidation(unittest.TestCase):

    def setUp(self):
        self.valid_transaction = {
            "transaction_id": 1,
            "amount": 100.0,
            "transaction_date": "2026-05-01T12:00:00Z",
            "status": "Success",
            "sender": {"full_name": "John"},
            "receiver": {"full_name": "Jane"}
        }

    def test_valid(self):
        valid, msg = validate_transaction(self.valid_transaction)
        self.assertTrue(valid)
        self.assertEqual(msg, "Valid transaction")

    def test_missing_field(self):
        data = self.valid_transaction.copy()
        del data["amount"]

        valid, msg = validate_transaction(data)
        self.assertFalse(valid)
        self.assertEqual(msg, "Missing field: amount")
    def test_invalid_amount(self):
        data = self.valid_transaction.copy()
        data["amount"] = -50

        valid, msg = validate_transaction(data)
        self.assertFalse(valid)
        self.assertEqual(msg, "Amount must be greater than 0")
    def test_invalid_sender(self):
        data = self.valid_transaction.copy()
        data["sender"] = {}

        valid, msg = validate_transaction(data)
        self.assertFalse(valid)


if __name__ == "__main__":
    unittest.main()