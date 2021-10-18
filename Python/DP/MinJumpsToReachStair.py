def min_jumps_to_reach_stair(n: int) -> int:
    arr = [0, 1, 1]
    for i in range(3, n + 1):
        arr.append(1 + min(min(arr[i - 1], arr[i - 2]), arr[i - 3]))
    # for i in range(1, n + 1):
    #     if i - 3 >= 0:
    #         arr.append(arr[i - 3] + 1)
    #     elif i - 2 >= 0:
    #         arr.append(arr[i - 2] + 1)
    #     else:
    #         arr.append(arr[i - 1] + 1)
    print(arr)
    return arr[n]


def main():
    n = int(input())
    print(min_jumps_to_reach_stair(n))


if __name__ == '__main__':
    main()
