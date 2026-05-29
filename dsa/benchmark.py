# dsa/benchmark.py

import time
from parser import parse_sms_xml
from search import linear_search, dictionary_lookup

import time

def benchmark(func, data):
    start = time.time()
    func(data)
    end = time.time()
    return end - start

transactions = parse_sms_xml("../data/modified_sms_v2.xml")

transaction_dict = {
    t["id"]: t for t in transactions
}

target = 20

start = time.perf_counter()
linear_search(transactions, target)
linear_time = time.perf_counter() - start

start = time.perf_counter()
dictionary_lookup(transaction_dict, target)
dict_time = time.perf_counter() - start

print(f"Linear Search: {linear_time}")
print(f"Dictionary Lookup: {dict_time}")