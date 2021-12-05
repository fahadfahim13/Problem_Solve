import heapq as hp


def frequency_sort(numbers: list[int]) -> list[int] or None:
    if numbers is None or len(numbers) <= 0:
        return None
    freq_arr = {}
    for i in numbers:
        if i in freq_arr:
            freq_arr[i] += 1
        else:
            freq_arr[i] = 1
    arr = []
    hp.heapify(arr)
    for i in freq_arr:
        hp.heappush(arr, (-freq_arr[i], i))
    print(arr)
    ans = []
    while len(arr):
        el = hp.heappop(arr)
        ans.append(el[1])
    return ans


def main():
    arr = [10, 7, 10, 6, 10, 7, 5]
    print(frequency_sort(arr))


if __name__ == '__main__':
    main()
