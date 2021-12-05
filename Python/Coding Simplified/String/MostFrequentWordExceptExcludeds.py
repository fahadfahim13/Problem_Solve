def most_frequent_word_except_excluded(string: str, excluded: list[str]) -> str or None:
    if string is None or excluded is None or len(string) == 0:
        return None
    freq_map = {}
    most_freq = 0
    most_freq_word = ""
    ans_array = string.split()
    for i in ans_array:
        if i not in excluded and i.lower() not in excluded:
            tmp = i.lower()
            if tmp in freq_map:
                freq_map[tmp] += 1
            else:
                freq_map[tmp] = 1
            if freq_map[tmp] > most_freq:
                most_freq = freq_map[tmp]
                most_freq_word = tmp
    for key in freq_map:
        if freq_map[key] == most_freq:
            print(key)
    return most_freq_word


def main():
    string = "Best items in category are samsung Lenovo Samsung items are nice but lenovo are cool"
    excluded = ["are", "is", "in", "but"]
    print(most_frequent_word_except_excluded(string, excluded))


if __name__ == '__main__':
    main()
