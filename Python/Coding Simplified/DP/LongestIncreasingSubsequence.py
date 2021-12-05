def longest_increasing_subsequence(arr: list) -> int:
    if not arr:
        return -1
    length = [1 for i in range(len(arr))]
    for i in range(len(arr)):
        for j in range(0, i):
            if length[i] < length[j] + 1 and arr[i] > arr[j]:
                length[i] = length[j] + 1
    print(length)
    return max(length)


def main():
    arr = [7, 1, 4, 8, 11, 2, 14, 3]
    print(longest_increasing_subsequence(arr))


if __name__ == '__main__':
    main()
