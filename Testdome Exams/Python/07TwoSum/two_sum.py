def find_two_sum(numbers, target_sum):
    check_set = {}
    for idx, number in enumerate(numbers):
        if target_sum - number in check_set and check_set[target_sum - number] != idx:
            return check_set[target_sum - number], idx
        check_set[number] = idx
    # :param numbers: (list of ints) The list of numbers.
    # :param target_sum: (int) The required target sum.
    # :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
    return None


def main():
    print(find_two_sum([3, 1, 5, 7, 5, 9], 10))


if __name__ == '__main__':
    main()
