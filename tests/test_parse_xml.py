import unittest
import os
from etl.parse_xml import parse_sms_xml

class TestXMLParsing(unittest.TestCase):

    def setUp(self):
        self.test_file = "test_sample.xml"
        content = """<?xml version="1.0"?><sms_records>
            <sms id="99" type="Transfer" amount="10.00" sender="A" receiver="B" timestamp="2026-05-30"/>
        </sms_records>"""
        with open(self.test_file, "w") as f:
            f.write(content)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_is_list_of_dicts(self):
        data = parse_sms_xml(self.test_file)
        self.assertIsInstance(data, list)
        self.assertIsInstance(data[0], dict)

    def test_contains_required_keys(self):
        data = parse_sms_xml(self.test_file)[0]
        for key in ["id", "type", "amount", "sender", "receiver", "timestamp"]:
            self.assertIn(key, data)

    def test_invalid_file_throws_error(self):
        with self.assertRaises(FileNotFoundError):
            parse_sms_xml("fake_file.xml")

if __name__ == "__main__":
    unittest.main()
