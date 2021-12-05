def segregate_even_and_odd(arr: list[int]) -> list[int] or None:
    if arr is None or len(arr) <= 0:
        return None
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] % 2 != 0 and arr[right] % 2 == 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        elif arr[left] % 2 == 0:
            left += 1
        else:
            right -= 1

    return arr


def main():
    arr = [2, 11, 1, 3, 6, 10, 4]
    print(segregate_even_and_odd(arr))


if __name__ == "__main__":
    main()
