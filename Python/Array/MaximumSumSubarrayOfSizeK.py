import math


def maximum_size_subarray_with_size_k(arr, size):
    max_sum = -math.inf
    left = 0
    right = size
    current_sum = sum(arr[i] for i in range(left, right))
    while right < len(arr):
        max_sum = max(max_sum, current_sum)
        current_sum = current_sum - arr[left] + arr[right]
        right += 1
        left += 1
    return max_sum


if __name__ == "__main__":
    arr = [1, 4, 20, 3, 10, 5]
    print(maximum_size_subarray_with_size_k(arr, 3))
