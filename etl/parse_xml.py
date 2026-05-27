import xml.etree.ElementTree as ET
import os
import re


# function to parse break a single raw sms into a python dictionary
def parse_sms_body(body_text):

    #fallback values 
    data = {
        "id": "unknown",
        "type": "other",
        "amount": 0.0,
        "sender": "unknown",
        "receiver": "unknown",
        "timestamp": ""
    }
    #safety check
    if not body_text:
        return data
    clean_body = body_text.strip()


    time_match = re.search(r"at\s+(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})", clean_body)
    if time_match:
        data["timestamp"] = time_match.group(1)

    # if received is in message then the recevier is "me"
    if "received" in clean_body.lower():
        data["type"] = "received"
        data["receiver"] = "Me"
        
    #removes commas and converts numbers to folating point
        amt_match = re.search(r"received\s+([\d,]+)\s*RWF", clean_body, re.IGNORECASE)
        if amt_match:
            data["amount"] = float(amt_match.group(1).replace(",", ""))
            
        snd_match = re.search(r"from\s+([^\(]+)", clean_body)
        if snd_match:
            data["sender"] = snd_match.group(1).strip()
            

        id_match = re.search(r"Transaction\s+Id:\s*(\d+)", clean_body, re.IGNORECASE)
        if id_match:
            data["id"] = id_match.group(1)

    # if text says payment or txid then the sender is "me"
    elif "payment" in clean_body.lower() or "txid" in clean_body.lower():
        data["type"] = "payment"
        data["sender"] = "Me"
        
        id_match = re.search(r"TxId:\s*(\d+)", clean_body, re.IGNORECASE)
        if id_match:
            data["id"] = id_match.group(1)
            
        
        amt_match = re.search(r"payment\s+of\s+([\d,]+)\s*RWF", clean_body, re.IGNORECASE)
        if amt_match:
            data["amount"] = float(amt_match.group(1).replace(",", ""))
            
        
        rcv_match = re.search(r"to\s+([^0-9]+)", clean_body)
        if rcv_match:
            recipient = rcv_match.group(1).replace("has been completed", "")
            data["receiver"] = recipient.strip()

    return data


def parse_sms_xml(file_path):
    #Opens file and process every message inside

    # if the filepath is wrong then to program stops
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The target XML file path was not found: {file_path}")

    # if xml file is formatted incorrectly then it shows an error
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
    except ET.ParseError as e:
        raise ValueError(f"Failed to parse XML file sequence: {e}")

    transactions = []
    
    
    for sms in root.findall('sms'):
        body_content = sms.get('body') or ""
        parsed_txn = parse_sms_body(body_content)
        
        
        if parsed_txn["id"] == "unknown":
            fallback_id = sms.get("date") or sms.get("date_sent")
            parsed_txn["id"] = f"FALLBACK_{fallback_id}"
            
        transactions.append(parsed_txn)
        
    return transactions
