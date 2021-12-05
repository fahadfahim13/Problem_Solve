def longest_palindrome_subsequence_recursive(string: str, start: int, end: int) -> int:
    if string is None or start > end:
        return 0
    if start == end:
        return 1
    if string[start] == string[end]:
        return 2 + longest_palindrome_subsequence_recursive(string, start + 1, end - 1)
    else:
        return max(longest_palindrome_subsequence_recursive(string, start, end - 1), longest_palindrome_subsequence_recursive(string, start + 1, end))


def longest_palindrome_subsequence_array(string: str) -> int:
    if string is None:
        return 0
    arr = [[0 for i in range(len(string))] for j in range(len(string))]
    for i in range(len(string)):
        arr[i][i] = 1
    for i in range(len(string) - 2, -1, -1):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                arr[i][j] = 2 + arr[i + 1][j - 1]
            else:
                arr[i][j] = max(arr[i + 1][j], arr[i][j - 1])
    return arr[0][-1]


def main():
    string = "abefcebac"
    print(longest_palindrome_subsequence_recursive(string, 0, len(string) - 1))
    print(longest_palindrome_subsequence_array(string))


if __name__ == '__main__':
    main()
