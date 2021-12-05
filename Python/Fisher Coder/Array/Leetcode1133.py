from collections import Counter


def largest_unique_number(arr: list[int]) -> int:
    count = Counter(arr)
    max_num = -1
    print(count)
    for i in count:
        if i > max_num and count[i] == 1:
            max_num = i
    return max_num


def largest_unique_number_simple(arr: list[int]) -> int:
    count_arr = [0 for i in range(1001)]
    for i in arr:
        count_arr[i] += 1
    for i in range(1000, 0, -1):
        if count_arr[i] == 1:
            return i
    return -1


def main():
    arr = [5, 7, 3, 9, 4, 9, 8, 3, 1]
    print(largest_unique_number(arr))
    print(largest_unique_number_simple(arr))


if __name__ == '__main__':
    main()
