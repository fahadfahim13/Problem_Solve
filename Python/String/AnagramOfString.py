def anagram_of_string(string1: str, string2: str) -> bool:
    if string1 is None or string2 is None or len(string1) <= 0 or len(string2) <= 0:
        return False
    string2_map = {}
    string1_map = {}
    for i in string2:
        if i not in string2_map:
            string2_map[i] = 1
        else:
            string2_map[i] += 1
    start = 0
    end = 0
    while start <= end < len(string1):
        if string1[end] not in string1_map:
            string1_map[string1[end]] = 1
        else:
            string1_map[string1[end]] += 1
        if end - start == len(string2) - 1:
            if string1_map == string2_map:
                print(string1[start: end+1])
                return True
            if string1_map[string1[start]] == 1:
                del string1_map[string1[start]]
            else:
                string1_map[string1[start]] -= 1
            start += 1
        end += 1
    return False


def main():
    string1 = "dbabcd"
    string2 = "cab"
    print(anagram_of_string(string1, string2))


if __name__ == '__main__':
    main()
