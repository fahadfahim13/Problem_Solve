def delete_min_string_to_palindrome(string: str) -> int:
    if string is None or len(string) == 0:
        return 0
    sub_arr = [[0 for i in range(len(string))] for j in range(len(string))]
    for i in range(len(string)):
        sub_arr[i][i] = 1
    start = 0
    end = len(string) - 1
    for i in range(end, start - 1, -1):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                sub_arr[i][j] = 2 + sub_arr[i + 1][j - 1]
            else:
                sub_arr[i][j] = max(sub_arr[i + 1][j], sub_arr[i][j - 1])
        print(sub_arr[i])
    return len(string) - sub_arr[start][end]


def main():
    string = "abcfbac"
    print(delete_min_string_to_palindrome(string))


if __name__ == '__main__':
    main()
