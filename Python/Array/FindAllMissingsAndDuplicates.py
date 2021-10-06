def find_all_missing_and_duplicates(arr: list[int]) -> (list[int], list[int]):
    missing = set()
    duplicates = set()
    i = 0
    while i < len(arr):
        j = arr[i] - 1
        if arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1
    for i in range(len(arr)):
        if arr[i] != i + 1:
            missing.add(i+1)
            duplicates.add(arr[i])
    return missing, duplicates


def main():
    arr = [2, 6, 4, 4, 3, 2]
    print(find_all_missing_and_duplicates(arr))


if __name__ == '__main__':
    main()