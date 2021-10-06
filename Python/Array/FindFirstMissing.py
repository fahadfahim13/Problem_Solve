def first_missing_positive(arr: list[int]) -> int or None:
    if arr is None or len(arr) <= 0:
        return None
    i = 0
    while i < len(arr):
        j = arr[i] - 1
        if 0 < arr[i] <= len(arr):
            if arr[i] != arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1

    for i in range(len(arr)):
        j = arr[i] - 1
        if arr[i] != arr[j]:
            return i + 1


def main():
    arr = [-2, 11, 1, -3, 2, 10, 4]
    print(first_missing_positive(arr))


if __name__ == "__main__":
    main()
