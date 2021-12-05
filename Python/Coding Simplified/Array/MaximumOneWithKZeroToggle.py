def maximum_sub_array_of_one_with_k_zero(arr: list[int], k: int) -> int:
    maximum_sub_array_length = 0
    start = 0
    zero_count = 0
    end = 0
    while end < len(arr):
        if arr[end] == 0:
            zero_count += 1
        while zero_count > k:
            if arr[start] == 0:
                zero_count -= 1
            start += 1
        end += 1
        maximum_sub_array_length = max(maximum_sub_array_length, end - start)
    return maximum_sub_array_length


def main():
    arr = [0, 1, 0, 1, 0, 1, 1, 1, 0]
    print(maximum_sub_array_of_one_with_k_zero(arr, 1))
    # print(arr[::-1])   # Re
    # arr.reverse()
    # print(arr)


if __name__ == "__main__":
    main()
