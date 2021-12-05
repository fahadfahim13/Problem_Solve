def subarray_sum_equals_k(arr, sum):
    current_sum = 0
    left = 0
    right = 0
    while right < len(arr):
        if current_sum > sum:
            current_sum -= arr[left]
            left += 1
        elif current_sum < sum:
            current_sum += arr[right]
            right += 1
        else:
            return arr[left:right]
        if left > right:
            break
    return None


if __name__ == "__main__":
    arr = [1, 4, 20, 3, 10, 5]
    print(subarray_sum_equals_k(arr, 33))
