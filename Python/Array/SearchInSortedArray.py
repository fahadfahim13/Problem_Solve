def search(arr, val):
    if arr is None:
        return None
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if val < arr[mid]:
            end = mid - 1
        elif val > arr[mid]:
            start = mid + 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    print(search(arr, 16))
