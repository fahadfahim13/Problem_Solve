def maximum_sum_increasing_subsequence(arr: list) -> int:
    if not arr:
        return -1
    _sum = [i for i in arr]
    print(_sum)
    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[i] > arr[j] and (_sum[j] + arr[i]) > _sum[i]:
                _sum[i] = _sum[j] + arr[i]
        print(_sum)
    print(_sum)
    return max(_sum)


def main():
    arr = [7, 1, 4, 8, 11, 2, 14, 3]
    print(maximum_sum_increasing_subsequence(arr))


if __name__ == '__main__':
    main()
