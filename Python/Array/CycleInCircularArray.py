def get_next_index(arr: list, index: int, prev_direction: bool) -> int:
    direction = arr[index] > 0
    if direction != prev_direction:
        return -1
    next_index = (index + arr[index]) % len(arr)
    if next_index == index:
        return -1
    return next_index


def cycle_in_circular_array(arr: list) -> bool:
    if arr is None or len(arr) <= 0:
        return False

    for i in range(len(arr)):
        slow = i
        fast = i
        direction = arr[i] > 0
        while True:
            slow = get_next_index(arr, slow, direction)
            if slow == -1:
                break
            fast = get_next_index(arr, fast, direction)
            if fast == -1:
                break
            fast = get_next_index(arr, fast, direction)
            if fast == -1:
                break
            if slow == fast:
                return True
    return False


def main():
    # arr = [2, -1, 1, 2, -1]
    arr = [4, 1, 1, 1]
    print(cycle_in_circular_array(arr))


if __name__ == "__main__":
    main()
