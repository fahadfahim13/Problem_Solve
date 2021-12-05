import math


def minimum_subarray_length_with_given_sum(arr, sum):
    left = 0
    right = 0
    current_sum = 0
    current_length = math.inf
    min_length = math.inf
    while len(arr) > right >= left:
        if current_sum < sum:
            current_sum += arr[right]
            if right < len(arr) - 1:
                right += 1
        elif current_sum > sum:
            current_sum -= arr[left]
            left += 1
        else:
            current_length = right - left if right > left else 1
            min_length = min(min_length, current_length)
            current_sum -= arr[left]
            left += 1

    return min_length


if __name__ == "__main__":
    arr = [3, 2, 5, 5, 3, 2, 10]
    print(minimum_subarray_length_with_given_sum(arr, 10))
