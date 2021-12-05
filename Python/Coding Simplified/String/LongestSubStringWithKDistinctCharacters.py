import math


def longest_sub_string_with_k_distinct_characters(string: str, k: int) -> str or None:
    if string is None or len(string) <= 0 or k is None or k <= 0:
        return None
    start = 0
    end = 0
    char_map = {}
    max_length = -math.inf
    while end < len(string):
        distinct_characters = sum(1 for i in char_map if char_map[i] > 0)
        if distinct_characters > k:
            char_map[str(string[start])] -= 1
            start += 1
        else:
            if string[end] not in char_map:
                char_map[string[end]] = 1
            else:
                char_map[string[end]] += 1
            max_length = max(max_length, end - start)
            end += 1

    return max_length


def main():
    string = "bccbababd"
    print(longest_sub_string_with_k_distinct_characters(string, 3))


if __name__ == '__main__':
    main()
