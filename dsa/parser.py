import os
import xml.etree.ElementTree as ET

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
FILE_PATH = os.path.join(BASE_DIR, "data", "modified_sms_v2.xml")


def parse_sms_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    sms_list = []

    for sms in root.findall("sms"):
        sms_list.append({
            "address": sms.get("address"),
            "body": sms.get("body"),
            "date": sms.get("date"),
            "type": sms.get("type")
        })

    return sms_list


if __name__ == "__main__":
    data = parse_sms_xml(FILE_PATH)
    print(f"Loaded {len(data)} messages")
    print(data[:3])