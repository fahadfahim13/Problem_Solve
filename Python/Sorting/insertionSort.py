def insertionSort(arr):
    if arr is None:
        return None

    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                # temp = arr[j]
                # arr[j] = arr[j - 1]
                # arr[j - 1] = temp
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break
    return arr


if __name__ == '__main__':
    arr = [23, 12, 15, 6, 13, 8, 3, 1, 2]
    print(insertionSort(arr))
