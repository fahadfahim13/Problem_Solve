def canReorderDoubled(arr: list[int]) -> bool:
    arr = sorted(arr)
    arr_map = {}
    print(arr)
    for i in range(len(arr)):
        if arr[i] not in arr_map:
            arr_map[arr[i]] = 1
        else:
            arr_map[arr[i]] += 1
    print(arr_map)
    for i in range(len(arr) - 1, -1, -1):
        print(arr[i], end=": ")
        if 2 * arr[i] in arr_map and arr[i] in arr_map:
            arr_map[2 * arr[i]] -= 1
            arr_map[arr[i]] -= 1
            if (2 * arr[i]) in arr_map and arr_map[2 * arr[i]] == 0:
                arr_map.pop(2 * arr[i])
            if arr[i] in arr_map and arr_map[arr[i]] == 0:
                arr_map.pop(arr[i])
        # elif (arr[i] // 2) in arr_map:
        #     arr_map[arr[i] // 2] -= 1
        #     arr_map[arr[i]] -= 1
        #     if arr_map[arr[i] // 2] == 0:
        #         arr_map.pop(arr[i] // 2)
        #     if arr_map[arr[i]] == 0:
        #         arr_map.pop(arr[i])
        # print(arr_map)
    return len(arr_map) == 0


def main():
    arr = [3, 1, 3, 6]
    # arr = [2, 1, 2, 6]
    # arr = [4, -2, 2, -4]
    # arr = [2, 4, 0, 0, 8, 1]
    # arr = [-6, -3]
    print(canReorderDoubled(arr))


if __name__ == '__main__':
    main()
