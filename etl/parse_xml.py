import xml.etree.ElementTree as ET
import os

def parse_sms_xml(file_path):
    """Parses modified_sms_v2.xml and converts attributes into dictionaries."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
        
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
    except ET.ParseError as e:
        raise ValueError(f"Invalid XML syntax: {e}")

    transactions = []

    for sms in root.findall('sms'):
        tx_data = {
            "id": sms.get('id', '').strip(),
            "type": sms.get('type', 'Unknown').strip(),
            "amount": sms.get('amount', '0.00').strip(),
            "sender": sms.get('sender', '').strip(),
            "receiver": sms.get('receiver', '').strip(),
            "timestamp": sms.get('timestamp', '').strip()
        }
        transactions.append(tx_data)
        
    return transactions

if __name__ == "__main__":
    try:
        data = parse_sms_xml("modified_sms_v2.xml")
        print(f"Success! Parsed {len(data)} records.")
    except Exception as e:
        print(f"Error: {e}")
