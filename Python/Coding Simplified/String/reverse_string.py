def reverse_string(string: str) -> str or None:
    if string is None or len(string) == 0:
        return None
    string_arr = list(string)
    length = len(string_arr)
    for i in range(0, length // 2):
        string_arr[i], string_arr[length - 1 - i] = string_arr[length - 1 - i], string_arr[i]
    print(string_arr)
    return ''.join(string_arr)


def main():
    string = "HelloWorld"
    print(reverse_string(string))


if __name__ == '__main__':
    main()
