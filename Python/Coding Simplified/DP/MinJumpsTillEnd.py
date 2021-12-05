import math


def min_jumps_till_end(arr: list[int]) -> int:
    if arr is None:
        return 0
    inf = 999999
    jump_arr = [inf for j in range(len(arr))]
    jump_arr[0] = 0
    for i in range(len(arr) - 1):
        j = i + 1
        while j <= i + arr[i] and j < len(arr):
            jump_arr[j] = min(jump_arr[j], 1 + jump_arr[i])
            j = j + 1
    return jump_arr[-1]


def main():
    arr = [1, 2, 1, 3, 2, 1, 2, 1]
    print(min_jumps_till_end(arr))


if __name__ == '__main__':
    main()
