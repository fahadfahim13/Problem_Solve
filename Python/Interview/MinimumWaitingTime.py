def minimum_waiting_time(arr: list) -> int or None:
    if arr is None:
        return None
    sum_nums = 0
    new_arr = sorted(arr)
    cumulative_sum = 0
    for i in range(0, len(new_arr)):
        print(cumulative_sum, end=" ")
        sum_nums += cumulative_sum
        cumulative_sum += new_arr[i]

    print()
    return sum_nums


def main():
    # arr = [1, 5, 4]
    # arr = [1, 5]
    arr = [6, 1, 2, 2, 3]
    print(minimum_waiting_time(arr))


if __name__ == '__main__':
    main()
