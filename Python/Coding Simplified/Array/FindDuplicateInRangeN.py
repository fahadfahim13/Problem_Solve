def find_duplicate_in_range_n(arr: list[int]) -> int or None:
    i = 0
    while i < len(arr):
        j = arr[i] - 1
        if arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1
    return arr[-1]


def main():
    arr = [2, 3, 4, 1, 2]
    print(find_duplicate_in_range_n(arr))


if __name__ == '__main__':
    main()
