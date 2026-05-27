import unittest
import os
from etl.parse_xml import parse_sms_xml

class TestXMLParsingSchema(unittest.TestCase):
    
    def setUp(self):
        """Builds local sandbox instances mimicking target system storage formats."""
        self.test_filename = "test_modified_sms_v2.xml"
        self.mock_xml_content = """<?xml version='1.0' encoding='utf-8'?>
        <smses count="2">
        <sms address="M-Money" date="1715351458724" body="You have received 2000 RWF from Jane Smith (*********013) on your mobile money account at 2024-05-10 16:30:51. Message from sender: . Your new balance:2000 RWF. Financial Transaction Id: 76662021700." />
        <sms address="M-Money" date="1715351506754" body="TxId: 73214484437. Your payment of 1,000 RWF to Jane Smith 12845 has been completed at 2024-05-10 16:31:39." />
        </smses>
        """
        with open(self.test_filename, "w", encoding="utf-8") as f:
            f.write(self.mock_xml_content)

    def tearDown(self):
        """Destroys temporary workspace configurations post testing."""
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_inbound_regex_extraction(self):
        """Validates nested elements on incoming deposit records."""
        records = parse_sms_xml(self.test_filename)
        self.assertEqual(len(records), 2)
        
        inbound_tx = records[0]
        self.assertEqual(inbound_tx["id"], "76662021700")
        self.assertEqual(inbound_tx["type"], "received")
        self.assertEqual(inbound_tx["amount"], 2000.0)
        self.assertEqual(inbound_tx["sender"], "Jane Smith")
        self.assertEqual(inbound_tx["receiver"], "Me")
        self.assertEqual(inbound_tx["timestamp"], "2024-05-10 16:30:51")

    def test_outbound_regex_extraction(self):
        """Validates nested elements on outgoing payment records."""
        records = parse_sms_xml(self.test_filename)
        
        outbound_tx = records[1]
        self.assertEqual(outbound_tx["id"], "73214484437")
        self.assertEqual(outbound_tx["type"], "payment")
        self.assertEqual(outbound_tx["amount"], 1000.0)
        self.assertEqual(outbound_tx["sender"], "Me")
        self.assertEqual(outbound_tx["receiver"], "Jane Smith")
        self.assertEqual(outbound_tx["timestamp"], "2024-05-10 16:31:39")

if __name__ == "__main__":
    unittest.main()
