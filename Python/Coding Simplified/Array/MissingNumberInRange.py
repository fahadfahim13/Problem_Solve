def missing_num(arr, n):
    if arr is None:
        return None
    sum = 0
    for i in arr:
        sum = sum + i
    supposed_sum = n * (n + 1) // 2
    return supposed_sum - sum


if __name__ == '__main__':
    arr = [4, 8, 6, 1, 2, 3, 7, 9]
    print(missing_num(arr, 9))
