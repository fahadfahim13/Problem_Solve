def findSpecialInteger(arr: list[int]) -> int:
    quarter = len(arr) // 4
    for i in range(len(arr)):
        if arr[i] == arr[i + quarter]:
            return arr[i]
    ###### Another Simple Solution ######
    # if len(arr) == 1:
    #     return arr[0]
    # count = {}
    # for i in arr:
    #     if i not in count:
    #         count[i] = 0
    #     else:
    #         count[i] += 1
    #         if count[i] >= len(arr) // 4:
    #             return i


def main():
    # arr = [1, 2, 2, 6, 6, 6, 6, 7, 10]
    arr = [1, 2, 3, 3]
    print(findSpecialInteger(arr))


if __name__ == '__main__':
    main()
