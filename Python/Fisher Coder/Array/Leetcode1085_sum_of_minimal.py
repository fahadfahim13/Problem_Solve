def sum_of_minimal(numbers: list[int]) -> int:
    if numbers is None or len(numbers) == 0:
        return 0
    smallest = min(numbers)
    total = 0
    num_arr = list(str(smallest))
    for num in num_arr:
        total += int(num)
    return 1 if total % 2 == 0 else 0


def main():
    arr = [55, 33, 44, 66, 88, 99]
    # arr = [34, 23, 1, 24, 75, 33, 54, 8]
    print(sum_of_minimal(arr))


if __name__ == '__main__':
    main()
