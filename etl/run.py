import time
from parse_xml import parse_sms_xml

# Linear search
def linear_search(tx_list, target_id):
    
    for tx in tx_list:
        if tx['id'] == target_id:
            return tx
    return None
# dictionary lookup
def dict_lookup(tx_dict, target_id):
    return tx_dict.get(target_id)

def run_benchmarks():
    xml_path = "modified_sms_v2.xml"
    try:
        tx_list = parse_sms_xml(xml_path)
    except Exception as e:
        try:
            tx_list = parse_sms_xml("../data/modified_sms_v2.xml")
        except:
            print(f"Benchmark aborted. Could not locate XML file: {e}")
            return

    tx_dict = {tx['id']: tx for tx in tx_list}
    
    target_id = tx_list[-1]['id'] if tx_list else "1"
    iterations = 50000

    print("-" * 50)
    print(f"Running Performance Benchmarks ({iterations:,} loops)...")
    print("-" * 50)

    # Time Linear Search
    start = time.perf_counter()
    for _ in range(iterations):
        linear_search(tx_list, target_id)
    linear_time = (time.perf_counter() - start) / iterations

    # Time Dictionary Lookup
    start = time.perf_counter()
    for _ in range(iterations):
        dict_lookup(tx_dict, target_id)
    dict_time = (time.perf_counter() - start) / iterations

    print(f"Linear Search Avg: {linear_time:.8f} seconds")
    print(f"Dictionary Lookup Avg: {dict_time:.8f} seconds")
    print(f"Result: Dictionary is {linear_time/dict_time:.1f}x faster!")
    print("-" * 50)

if __name__ == "__main__":
    run_benchmarks()
