import math


def longest_sub_string_with_no_repeating(string: str) -> str or None:
    if string is None or len(string) <= 0:
        return None
    if len(string) == 1:
        return 1
    start = 0
    end = 0
    char_map = {}
    max_length = -math.inf
    while end < len(string):
        if string[end] not in char_map:
            char_map[string[end]] = [1, end]
            end += 1
        else:
            start_next = char_map[string[end]][1] + 1
            while start < start_next:
                del char_map[string[start]]
                start += 1
        max_length = max(max_length, end - start)

    return max_length


def main():
    string = "babccbacda"
    print(longest_sub_string_with_no_repeating(string))


if __name__ == '__main__':
    main()
