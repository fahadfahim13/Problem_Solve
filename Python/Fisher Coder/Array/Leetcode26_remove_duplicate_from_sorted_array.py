def remove_duplicate(sorted_arr: list[int]) -> list[int]:
    # return list(set(sorted_arr))
    slow = 0
    fast = 1
    n = len(sorted_arr)
    while slow < n and fast < n:
        if sorted_arr[fast] != sorted_arr[slow]:
            sorted_arr[slow + 1] = sorted_arr[fast]
            slow += 1
            fast += 1
        else:
            fast += 1
    for i in range(slow + 1, fast):
        sorted_arr.pop()
    return sorted_arr


def main():
    arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(remove_duplicate(arr))


if __name__ == '__main__':
    main()
