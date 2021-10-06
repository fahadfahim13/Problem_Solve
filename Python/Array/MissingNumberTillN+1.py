def missing_number_till_n_plus_1(arr: list[int]) -> int or bool or None:
    if arr is None or len(arr) <= 0:
        return None
    total = sum(i for i in arr)
    expected_sum = (len(arr) + 1) * (len(arr) + 2) // 2
    return expected_sum - total


def missing_number_with_sort(arr: list[int]) -> int or None:
    if arr is None or len(arr) <= 0:
        return None
    i = 0
    while i < len(arr):
        new_index = arr[i] - 1
        if i != new_index and arr[i] != len(arr) + 1:
            arr[i], arr[new_index] = arr[new_index], arr[i]
        else:
            i += 1

    for i in range(len(arr)):
        if arr[i] != i + 1:
            return i + 1


def main():
    arr = [3, 4, 5, 6, 1]
    print(missing_number_till_n_plus_1(arr))
    print(missing_number_with_sort(arr))


if __name__ == '__main__':
    main()
