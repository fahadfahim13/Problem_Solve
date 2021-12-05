def first_k_missing_numbers(arr: list[int], k) -> list[int] or None:
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
    total_missing = []

    for i in range(len(arr)):
        if arr[i] != i + 1:
            total_missing.append(i + 1)
        elif not 0 < arr[i] <= len(arr):
            total_missing.append(i + 1)

    while len(total_missing) < k:
        total_missing.append(total_missing[-1] + 1)

    return total_missing


def main():
    arr = [-2, 11, 1, -3, 2, 10, 4]
    print(first_k_missing_numbers(arr, 5))


if __name__ == "__main__":
    main()
