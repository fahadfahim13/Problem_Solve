import numpy as np


def get_new_array(arr: list[int]) -> list[int]:
    new_arr = [arr[0]]
    for i in range(1, len(arr) - 1):
        if arr[i - 1] > arr[i] < arr[i + 1]:
            new_arr.append(arr[i] + 1)
        elif arr[i - 1] < arr[i] > arr[i + 1]:
            new_arr.append(arr[i] - 1)
        else:
            new_arr.append(arr[i])
    new_arr.append(arr[-1])
    return new_arr


def array_transformation(arr: list[int]) -> list[int]:
    prev_arr = arr
    new_arr = get_new_array(arr)
    while not np.array_equal(np.array(new_arr), np.array(prev_arr)):
        prev_arr = new_arr
        new_arr = get_new_array(new_arr)
    return new_arr


def main():
    # arr = [6, 2, 3, 4]
    arr = [1, 6, 3, 4, 3, 5]
    print(array_transformation(arr))


if __name__ == '__main__':
    main()
