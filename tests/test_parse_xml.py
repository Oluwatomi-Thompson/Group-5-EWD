import unittest
from etl.parse_xml import parse_xml


class TestXML(unittest.TestCase):

    def test_parse(self):
        data = parse_xml("modified_sms_v2.xml")
        self.assertTrue(isinstance(data, list))


if __name__ == "__main__":
    unittest.main()