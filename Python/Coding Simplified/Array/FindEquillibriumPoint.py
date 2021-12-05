import math


def find_equillibrium_point(arr):
    if arr is None:
        return None
    total_sum = 0
    for i in arr:
        total_sum += i
    sum = 0
    for i in range(0, len(arr)):
        sum += arr[i]
        total_sum -= arr[i]
        if math.fabs(total_sum - sum) == arr[i]:
            return i


if __name__ == '__main__':
    arr = [2, 6, 7, 0, 8]
    print(find_equillibrium_point(arr))