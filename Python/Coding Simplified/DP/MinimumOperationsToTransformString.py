def minimum_operations_to_transform_string(str1: str, str2: str) -> int:
    small_arr = [0 for i in range(len(str1) + 1)]
    arr = [small_arr for j in range(len(str2) + 1)]
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[j - 1] == str1[i - 1]:
                arr[i][j] = arr[i - 1][j - 1]
            else:
                arr[i][j] = min(min(arr[i - 1][j], arr[i][j - 1]), arr[i - 1][j - 1])

    maxi = 0
    for i in range(len(str2) + 1):
        maxi = max(arr[i])
    return maxi


def main():
    str1 = "baute"
    str2 = "baatg"
    print(minimum_operations_to_transform_string(str1, str2))


if __name__ == '__main__':
    main()
