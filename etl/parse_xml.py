import xml.etree.ElementTree as ET
import os

def parse_sms_xml(file_path="data/modified_sms_v2.xml"):
    """
    Parses the modified_sms_v2.xml file from the data directory.
    Correctly extracts transaction records stored as XML attributes.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The XML file was not found at: {file_path}")
        
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
    except ET.ParseError as e:
        raise ValueError(f"Failed to parse invalid XML data: {e}")

    transactions = []
    
    # targets the sms elements and check their  attributes
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
    # Local verification block
    try:
        data = parse_sms_xml("data/modified_sms_v2.xml")
        print(f"[SUCCESS] Parsed {len(data)} records cleanly from data folder.")
    except Exception as e:
        print(f"[ERROR] Run failed: {e}")
