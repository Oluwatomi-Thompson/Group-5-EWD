
# tests/test_clean_normalize.py
import unittest
from api.schemas import validate_transaction 

class TestTransactionValidation(unittest.TestCase):
    def setUp(self):
        self.valid_transaction = {
            "id": 1,
            "type": "payment",
            "amount": "1500.50",
            "sender": "Nyayath",
            "receiver": "Elizabeth",
            "timestamp": "2026-05-01T12:00:00"
        }
    def test_valid_transaction(self):
        valid, message = validate_transaction (
            self.valid_transaction
            )
        self.assertTrue(valid)
        self.assertEqual(
            message, 
            "payload validated successfully"
            )
        
        def test_missing_field(self):
            payload = self.valid_transaction.copy()
            del payload["amount"]
            valid, message = validate_transaction(payload)
            self.assertFalse(valid)
            self.assertEqual(
                message, 
                "Amount must be numeric and  greater than zero"
            
                )
        def test_invalid_amount(self):
            payload = self.valid_transaction.copy()
            payload["amount"] = "-100"
            valid, message = validate_transaction(payload)
            self.assertFalse(valid)
            self.assertEqual( 
                message, 
                "Amount cannot be negative"
                )
        def test_invalid_timestamp(self):
            payload = self.valid_transaction.copy()
            payload["timestamp"] = "2026-05-01 12:00:00"
            valid, message = validate_transaction(payload)
            self.assertFalse(valid)
            self.assertEqual(
                message, 
                "Timestamp format should be YYYY-MM-DDTHH:MM:SS"
                )
            def test_empty_sender(self):
                payload = self.valid_transaction.copy()
                payload["sender"] = "   "
                valid, message = validate_transaction(payload)
                self.assertFalse(valid)
                self.assertEqual(
                    message, 
                    "Sender cannot be empty"
                    )
            def test_empty_receiver(self):
                payload = self.valid_transaction.copy()
                payload["receiver"] = "   "
                valid, message = validate_transaction(payload)
                self.assertFalse(valid)
                self.assertEqual(
                    message, 
                    "Receiver cannot be empty"
                    )
if __name__ == "__main__":
    unittest.main()