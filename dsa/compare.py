from dsa.search import build_index, dict_lookup, linear_search
import time


def compare(data, tid):

    start = time.time()
    linear_search(data, tid)
    t1 = time.time() - start

    index = build_index(data)

    start = time.time()
    dict_lookup(index, tid)
    t2 = time.time() - start

    return t1, t2