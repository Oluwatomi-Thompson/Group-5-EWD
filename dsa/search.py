# dsa/search.py

def linear_search(transactions, target_id):

    for transaction in transactions:
        if transaction["id"] == target_id:
            return transaction

    return None


def dictionary_lookup(transaction_dict, target_id):

    return transaction_dict.get(target_id)

def search_sms(data, keyword):
    return [sms for sms in data if keyword.lower() in sms["message"].lower()]