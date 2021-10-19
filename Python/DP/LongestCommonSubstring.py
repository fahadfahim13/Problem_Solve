def longest_common_substring(str1: str, str2: str) -> int:
    small_arr = [0 for i in range(0, len(str1) + 1)]
    arr = [small_arr for i in range(0, len(str2) + 1)]
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str1[j - 1]:
                arr[i][j] = 1 + arr[i - 1][j - 1]

    maxi = 0
    for i in range(0, len(str2) + 1):
        print(arr[i])
        maxi = max(arr[i])
    return maxi


def main():
    str1 = "fsfdfdsabcdefgtret"
    str2 = "bcdefghhot"
    print(longest_common_substring(str1, str2))


if __name__ == '__main__':
    main()
