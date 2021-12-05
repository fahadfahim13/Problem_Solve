def find_corrupt_pair(arr: list[int]) -> (int, int) or None:
    if arr is None or len(arr) <= 0:
        return None
    i = 0
    while i < len(arr):
        j = arr[i] - 1
        if arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1

    for i in range(len(arr)):
        if arr[i] != i + 1:
            return i + 1, arr[i]


def main():
    arr = [4, 3, 4, 2, 1]
    print(find_corrupt_pair(arr))


if __name__ == "__main__":
    main()
