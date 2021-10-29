def longest_palindromic_substring_recursive(string: str, start: int, end: int) -> int:
    if string is None or start > end:
        return 0
    if start == end:
        return 1
    if string[start] == string[end]:
        mid_len = end - start - 1
        if longest_palindromic_substring_recursive(string, start + 1, end - 1) == mid_len:
            return mid_len + 2
    return max(longest_palindromic_substring_recursive(string, start + 1, end),
               longest_palindromic_substring_recursive(string, start, end - 1))


def main():
    string = "abbcbbgbat"
    print(longest_palindromic_substring_recursive(string, 0, len(string) - 1))


if __name__ == '__main__':
    main()
