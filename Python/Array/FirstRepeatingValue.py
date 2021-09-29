def first_repeating_value(arr):
    if arr is None:
        return None
    numbers = {}

    for i in arr:
        if i in numbers:
            return i
        numbers[i] = 1

    return None


if __name__ == "__main__":
    arr = [2, 3, 4, 3, 4, 3, 5, 7]
    print(first_repeating_value(arr))