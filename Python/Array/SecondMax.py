import math


def second_max(arr: list) -> int or None:
    if arr is None or len(arr) == 0:
        return None
    maximum = - math.inf
    second_maximum = - math.inf
    for i in arr:
        if i > maximum:
            second_maximum = maximum
            maximum = i
        elif maximum > i > second_maximum:
            second_maximum = i

    return second_maximum


def main():
    # arr = [1, 2, 3, 4, 5]
    arr = [5, 1, 2, 4, 3, 5]
    print(second_max(arr))


if __name__ == "__main__":
    main()
