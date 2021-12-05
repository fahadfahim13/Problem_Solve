def longest_common_subsequence(str1: str, str2: str) -> int:
    small_arr = [0 for i in range(len(str1) + 1)]
    arr = [small_arr for j in range(len(str2) + 1)]
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            arr[i][j] = (arr[i - 1][j - 1] + 1) if str1[j - 1] == str2[i - 1] else max(arr[i - 1][j], arr[i][j - 1])

    return arr[-1][-1]


def main():
    str1 = "abcdefg"
    str2 = "abdft"
    print(longest_common_subsequence(str1, str2))


if __name__ == '__main__':
    main()
