def delete_min_string_to_palindrome(string: str) -> int:
    if string is None or len(string) == 0:
        return 0


def main():
    string = "abcfbac"
    print(delete_min_string_to_palindrome(string))


if __name__ == '__main__':
    main()
