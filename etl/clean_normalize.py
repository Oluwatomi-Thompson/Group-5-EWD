def clean_sms_data(sms_list):
    cleaned = []

    for sms in sms_list:
        body = sms.get("body")

        if not body:
            continue

        cleaned.append({
            "address": sms["address"],
            "body": body.strip().lower(),
            "date": sms["date"],
            "type": sms["type"]
        })

    return cleaned