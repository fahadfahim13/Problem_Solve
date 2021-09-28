def sort_array_of_0_1_2(arr):
    if arr is None:
        return None
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            if arr[low]:
                arr[mid], arr[low] = arr[low], arr[mid]
            mid += 1
            low += 1
        elif arr[mid] == 1:
            mid += 1
        elif arr[mid] == 2:
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1

    return arr


if __name__ == '__main__':
    arr = [0, 1, 2, 2, 1, 1, 1, 2, 0, 1]
    print(sort_array_of_0_1_2(arr))
