def two_sum(arr, sum):
    if arr is None or sum is None:
        return None

    numbers = {}
    for i in arr:
        if (sum - i) in numbers:
            return i, sum - i
        if i not in numbers:
            numbers[i] = 1

    return False


if __name__ == '__main__':
    arr = [12, 3, 5, 1, 9, 7]
    print(two_sum(arr, 10))