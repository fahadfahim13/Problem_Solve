def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = right
    while i < j:
        while i < right and arr[i] < arr[pivot]:
            i += 1
        while j > left and arr[j] > arr[pivot]:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > arr[pivot]:
        arr[i], arr[pivot] = arr[pivot], arr[i]

    return i


def quick_sort(arr, left, right):
    if left < right:
        part = partition(arr, left, right)
        quick_sort(arr, left, part - 1)
        quick_sort(arr, part + 1, right)


if __name__ == '__main__':
    arr = [22, 11, 88, 66, 55, 77, 33, 44]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)
