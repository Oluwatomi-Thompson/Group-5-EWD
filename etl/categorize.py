def categorize_sms(sms_list):
    categorized = []

    for sms in sms_list:
        text = sms["body"]

        if any(word in text for word in ["loan", "bank", "money"]):
            category = "finance"
        elif any(word in text for word in ["code", "otp", "verification"]):
            category = "security"
        elif "hello" in text or "hi" in text:
            category = "personal"
        else:
            category = "other"

        sms["category"] = category
        categorized.append(sms)

    return categorized