import math


def maximum_sum_subarray(arr):
    current_sum = 0
    max_sum = -math.inf
    is_all_neg = False
    max_el = -math.inf
    for i in arr:
        if i > 0:
            is_all_neg = True
        max_el = max(max_el, i)
        current_sum = current_sum + i
        if current_sum < 0:
            current_sum = 0
            continue
        max_sum = max(current_sum, max_sum)

    if not is_all_neg:
        return max_el
    return max_sum


if __name__ == '__main__':
    arr = [-3, 2, -7, 6, -2, 4, -8, 5]
    print(maximum_sum_subarray(arr))