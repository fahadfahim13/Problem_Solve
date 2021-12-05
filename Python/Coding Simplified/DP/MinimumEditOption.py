def min_edit_option(string1: str, string2: str) -> int or None:
    if string2 is None and string1 is None:
        return 0
    elif string2 is None:
        return len(string1)
    elif string1 is None:
        return len(string2)
    else:
        len1 = len(string1)
        len2 = len(string2)
        arr = [[0 for i in range(len1 + 1)] for j in range(len2 + 1)]
        for i in range(1, len2 + 1):
            for j in range(1, len1 + 1):
                if string1[j - 1] == string2[i - 1]:
                    tmp = arr[i - 1][j - 1]
                else:
                    min_num = min(min(arr[i - 1][j - 1], arr[i - 1][j]), arr[i][j - 1])
                    tmp = 1 + min_num
                arr[i][j] = tmp

        for i in range(len2 + 1):
            print(arr[i])
        return arr[-1][-1]


def main():
    string1 = "bat"
    string2 = "but"
    print(min_edit_option(string1, string2))


if __name__ == '__main__':
    main()
