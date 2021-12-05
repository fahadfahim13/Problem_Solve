def total_palindrome_sub_string(string: str) -> int:
    if string is None or len(string) == 0:
        return 0
    sub_arr = [[False for i in range(len(string))] for j in range(len(string))]
    total = 0
    for i in range(len(string)):
        sub_arr[i][i] = True
        total += 1

    print(sub_arr[-1])
    for i in range(len(string) - 2, -1, -1):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                if sub_arr[i + 1][j - 1] or j - i == 1:
                    sub_arr[i][j] = True
                    total += 1
            else:
                sub_arr[i][j] = False
        print(sub_arr[i])

    return total


def main():
    string = "bcacbf"
    print(total_palindrome_sub_string(string))


if __name__ == '__main__':
    main()

