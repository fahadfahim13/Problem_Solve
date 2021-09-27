def bubbleSort(arr):
    if arr is None:
        return None
    for i in range(0, len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    return arr


if __name__ == '__main__':
    arr = [12, 45, 2, 54, 6, 23, 10, 19]
    print(bubbleSort(arr))
