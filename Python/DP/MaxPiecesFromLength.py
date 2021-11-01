def max_pieces_from_length(arr: list[int], length: int) -> int:
    if arr is None or length is None:
        return 0
    pc_arr = [[0 for i in range(length + 1)] for j in range(len(arr))]
    for i in range(len(arr)):
        for j in range(length + 1):
            if i > 0:
                if j < arr[i]:
                    pc_arr[i][j] = pc_arr[i - 1][j]
                else:
                    pc_arr[i][j] = max(pc_arr[i - 1][j], 1 + pc_arr[i][j - arr[i]])
            else:
                if j == arr[i]:
                    pc_arr[i][j] = 1
        print(pc_arr[i])
    return pc_arr[-1][-1]


def main():
    arr = [4, 2, 3, 5]
    given_sum = 7
    print(max_pieces_from_length(arr, given_sum))


if __name__ == '__main__':
    main()
