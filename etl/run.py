import time
from parse_xml import parse_sms_xml

def linear_search(tx_list, target_id):
    for tx in tx_list:
        if tx['id'] == target_id:
            return tx
    return None

def dict_lookup(tx_dict, target_id):
    return tx_dict.get(target_id)

def run_benchmarks():
    # Load data using your parsing script
    tx_list = parse_sms_xml("data/modified_sms_v2.xml")
    
    # Map the list items to a dictionary structure
    tx_dict = {tx['id']: tx for tx in tx_list}
    
    # Target the last transaction ID in the dataset
    target_id = tx_list[-1]['id']

    # 1. Track Linear Search Time
    start_linear = time.perf_counter()
    linear_search(tx_list, target_id)
    end_linear = time.perf_counter()
    linear_time = end_linear - start_linear

    # 2. Track Dictionary Lookup Time
    start_dict = time.perf_counter()
    dict_lookup(tx_dict, target_id)
    end_dict = time.perf_counter()
    dict_time = end_dict - start_dict

    # Print raw speed results directly
    print("Linear Search Time:", linear_time, "seconds")
    print("Dictionary Lookup Time:", dict_time, "seconds")

if __name__ == "__main__":
    run_benchmarks()