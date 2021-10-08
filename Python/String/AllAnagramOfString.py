def all_anagram_of_a_string(string1: str, string2: str) -> list[str] or None:
    if string1 is None or string2 is None or len(string1) <= 0 or len(string2) <= 0:
        return None
    ans_strings = []
    string2_map = {}
    for i in string2:
        if i in string2_map:
            string2_map[i] += 1
        else:
            string2_map[i] = 1
    string1_map = {}
    start = 0
    end = 0
    while start <= end < len(string1):
        if string1[end] not in string1_map:
            string1_map[string1[end]] = 1
        else:
            string1_map[string1[end]] += 1

        if (end - start) == len(string2) - 1:
            if string1_map == string2_map:
                temp = string1[start:end+1]
                ans_strings.append(temp)
            if string1_map[string1[start]] == 1:
                del string1_map[string1[start]]
            else:
                string1_map[string1[start]] -= 1
            start += 1
        end += 1
    return ans_strings


def main():
    string1 = "bcdcbabcbd"
    string2 = "abc"
    print(all_anagram_of_a_string(string1, string2))


if __name__ == '__main__':
    main()
