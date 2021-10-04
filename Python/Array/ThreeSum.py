def two_sum(arr, k):
    if arr is None or k is None or len(arr) <= 0:
        return None, None
    freq = {}
    for i in arr:
        if i not in freq:
            freq[i] = 1

    for i in arr:
        if k - i in arr and i != k - i:
            return i, k - i
    return None, None


def three_sum(arr, k):
    if arr is None or k is None or len(arr) <= 0:
        return None
    arr = sorted(arr)
    for i in range(0, len(arr) - 2):
        start = i + 1
        end = len(arr) - 1
        while start < end:
            if (arr[start] + arr[end] + arr[i]) == k:
                print(arr[i], arr[start], arr[end])
                start += 1
                end -= 1
            elif (arr[start] + arr[end] + arr[i]) > k:
                end -= 1
            else:
                start += 1

    ####### With two sum function
    # for i in range(0, len(arr) - 2):
    #     second, third = two_sum(arr[i+1:], k - arr[i])
    #     if second is not None and third is not None:
    #         print(arr[i], second, third)


def main():
    arr = [1, 2, -3, 4, -2, -1]
    three_sum(arr, 1)


if __name__ == "__main__":
    main()
