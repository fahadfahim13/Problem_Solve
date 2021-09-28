def selection_sort(arr):
    if arr is None:
        return None

    for i in range(0, len(arr) - 1):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


if __name__ == '__main__':
    arr = [23, 13, 5, 16, 3, 2, 1, 10, 9]
    print(selection_sort(arr))
