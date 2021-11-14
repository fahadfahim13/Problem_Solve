import heapq as hp


def top_k_frequent_numbers_min_heap(numbers: list[int], k: int) -> list[int] or int:
    freq = {}
    for i in numbers:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    arr = []
    hp.heapify(arr)
    # print(freq)
    c = 0
    for i in freq:
        # print(i, freq[i])
        if c >= k:
            break
        hp.heappush(arr, (freq[i], i))
        c += 1
    largest = hp.heappop(arr)
    hp.heappush(arr, largest)
    # print(arr)
    c = 0
    for i in freq:
        c += 1
        if c <= k:
            continue
        if freq[i] > largest[0]:
            hp.heappop(arr)
            hp.heappush(arr, (freq[i], i))
            largest = hp.heappop(arr)
            hp.heappush(arr, largest)
    ans = []
    for i in range(k):
        el = hp.heappop(arr)
        ans.append(el[1])
    return ans


def top_k_frequent_numbers(numbers: list[int], k: int) -> list[int] or int:
    freq = {}
    for i in numbers:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    arr = []
    hp.heapify(arr)
    for i in freq:
        hp.heappush(arr, (-freq[i], i))
    # print(arr)
    ans = []
    for i in range(k):
        el = hp.heappop(arr)
        ans.append(el[1])
    return ans


def main():
    arr = [8, 10, 7, 8, 11, 30, 11, 8, 38, 11, 2, 45, 2, 8]
    k = 3
    print(top_k_frequent_numbers(arr, k))
    print(top_k_frequent_numbers_min_heap(arr, k))


if __name__ == '__main__':
    main()
