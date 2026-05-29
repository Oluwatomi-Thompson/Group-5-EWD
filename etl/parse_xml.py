from xml.etree import ElementTree as ET

def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    records = []

    for item in root:
        data = {}
        for child in item:
            data[child.tag] = child.text
        records.append(data)

    return records