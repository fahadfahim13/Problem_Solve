from bisect import bisect_left


def count_numbers(sorted_list, less_than):
    # begin = 0
    # end = len(sorted_list) - 1
    # mid = (begin + end) // 2
    # while begin <= end:
    #     if less_than == sorted_list[mid]:
    #         return mid
    #     elif less_than > sorted_list[mid]:
    #         begin = mid + 1
    #         mid = (begin + end) // 2
    #     elif less_than < sorted_list[mid]:
    #         end = mid - 1
    #         mid = (begin + end) // 2
    # return begin
    return bisect_left(sorted_list, less_than)


def main():
    sorted_list = [1, 3, 4, 5, 7]
    print(count_numbers(sorted_list, 0))  # should print 2


if __name__ == "__main__":
    main()
