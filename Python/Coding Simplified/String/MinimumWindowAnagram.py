import math
from collections import Counter


def compare_dictionary_values(big_dict: dict, small_dict: dict) -> bool:
    if big_dict is None or small_dict is None:
        return False
    # print(big_dict, small_dict)
    for i in small_dict:
        if i not in big_dict:
            return False
        if small_dict[i] > big_dict[i]:
            return False
    return True


def smallest_sub_string_with_anagram(big_string: str, pattern: str) -> str or None:
    if big_string is None or pattern is None or len(big_string) <= 0 or len(pattern) <= 0:
        return None
    pattern_map = Counter(pattern)
    start, end, matched = 0, 0, 0
    string_map = {}
    min_len = math.inf
    check_equal = False
    output_string = ""
    while start <= end < len(big_string):
        if big_string[end] in pattern_map:
            pattern_map[big_string[end]] -= 1
            if pattern_map[big_string[end]] >= 0:
                matched += 1
        while start < end and matched == len(pattern):
            if end - start < min_len:
                min_len = end - start + 1
                output_string = big_string[start:end+1]
            if big_string[start] in pattern_map:
                pattern_map[big_string[start]] += 1
                if pattern_map[big_string[start]] > 0:
                    matched -= 1
            start += 1
        end += 1
    print(output_string)
    return min_len


def main():
    # string = "bcdcbabcbd"
    # string = "abbaacdbcedab"
    string = "badeaebbbcabbae"
    pattern = "aabc"
    print(smallest_sub_string_with_anagram(string, pattern))


if __name__ == '__main__':
    main()
