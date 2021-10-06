def segregate_zero_and_one(arr:list[int]) -> list[int] or None:
    if arr is None or len(arr) <= 0:
        return None
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] == 1 and arr[right] == 0:
            arr[left], arr[right] = arr[right], arr[left]
        elif arr[left] == 1:
            right -= 1
        else:
            left += 1

    return arr


def main():
    arr = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1]
    print(segregate_zero_and_one(arr))


if __name__ == "__main__":
    main()
