import math


def largest_sum(arr):
    if arr is None:
        return 0
    current_max = - math.inf
    max_till_now = - math.inf
    for i in arr:
        current_max = max(current_max + i, i)
        max_till_now = max(current_max, max_till_now)
    
    return max_till_now


if __name__ == '__main__':
    arr = [-3, -4, 4, -1, -2, 1, 5, -3]
    print(largest_sum(arr))
    