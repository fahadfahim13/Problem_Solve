import math


def max_multiplication(arr):
    if len(arr) <= 1:
        return -1
    if len(arr) == 2:
        return arr[0] * arr[1]
    maxi = -math.inf
    second_max = -math.inf
    mini = math.inf
    second_min = math.inf

    for i in arr:
        if i > maxi:
            second_max = maxi
            maxi = i
        if i < mini:
            second_min = mini
            mini = i

    return max(mini * second_min, maxi * second_max)


if __name__ == '__main__':
    arr = [-4, 7, 18, 2, 5]
    print(max_multiplication(arr))
