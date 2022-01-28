def min_abs_diff(arr: list[int]) -> list[list[int]]:
    numbers = sorted(arr)
    min_diff = numbers[1] - numbers[0]
    res_arr = [[numbers[0], numbers[1]]]
    for i in range(2, len(numbers)):
        if (numbers[i] - numbers[i - 1]) == min_diff:
            res_arr.append([numbers[i-1], numbers[i]])
        elif (numbers[i] - numbers[i - 1]) < min_diff:
            min_diff = numbers[i] - numbers[i - 1]
            res_arr = [[numbers[i-1], numbers[i]]]
    return res_arr


def main():
    arr = [3, 8, -10, 23, 19, -4, -14, 27]
    print(min_abs_diff(arr))


if __name__ == '__main__':
    main()
