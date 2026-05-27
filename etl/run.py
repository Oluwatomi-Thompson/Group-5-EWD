import time
from parse_xml import parse_sms_xml

def linear_search(data_list, target_id):
    for item in data_list:
        if item["id"] == target_id:
            return item
    return None

def dictionary_lookup(data_dict, target_id):
    return data_dict.get(target_id)

def run_benchmark():
    print("Running System profiles")

    try:
        transactions_list = parse_sms_xml("modified_sms_v2.xml")
        print(f"Dataset confirmed.")
    except Exception:
        print("Dataset cannot be found. running synthetic benchmark vectors")
        transactions_list = [
            {
                "id": str(76662021700 + i),
                "type": "received" if i % 2 == 0 else "payment",
                "amount": float(1000 * i),
                "sender": "Jane Smith" if i % 2 == 0 else "Me",
                "receiver": "Me" if i % 2 == 0 else "Jane Smith",
                "timestamp": "2024-05-10 16:30:51"
            }
            for i in range(1, 30)
        ]

    transactions_dict = {tx["id"]: tx for tx in transactions_list}
    
    sample_ids = [tx["id"] for tx in transactions_list[:20]]
    loops = 40000 
    
    print(f"Running index loops over {loops:,} iterations against sample sets")

    #  linear Search
    t_start = time.perf_counter()
    for _ in range(loops):
        for target_id in sample_ids:
            linear_search(transactions_list, target_id)
    linear_time = time.perf_counter() - t_start

    # time Dictionary Lookup
    t_start = time.perf_counter()
    for _ in range(loops):
        for target_id in sample_ids:
            dictionary_lookup(transactions_dict, target_id)
    dict_time = time.perf_counter() - t_start

    print(f"Linear Search Compute Profile: {linear_time:.6f} seconds")
    print(f"Hash Mapping Compute Profile: {dict_time:.6f} seconds")
    
    if dict_time > 0:
        performance_gain = linear_time / dict_time
        print(f"Key Hash Dictionary is {performance_gain:.2f}x faster.")

if __name__ == "__main__":
    run_benchmark()
