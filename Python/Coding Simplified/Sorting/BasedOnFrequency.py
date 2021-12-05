from queue import PriorityQueue
import heapq
from functools import cmp_to_key


def sort_based_on_frequency(arr):
    freq = {}
    q = PriorityQueue()
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    print(freq)
    new_arr = sorted(arr, key=cmp_to_key(lambda it1, it2: it2 - it1))  # Compare based on value
    new_arr = sorted(new_arr, key=cmp_to_key(lambda it1, it2: freq[it2] - freq[it1]))
    # new_arr = sorted(new_arr, key= lambda it: new_arr.index(it)) # Compare based on index

    return new_arr
    

def main():
    arr = [10, 7, 10, 11, 10, 7, 5, 6, 4, 4, 4, 4]
    new_arr = sort_based_on_frequency(arr)
    print(new_arr)


if __name__ == '__main__':
    main()
