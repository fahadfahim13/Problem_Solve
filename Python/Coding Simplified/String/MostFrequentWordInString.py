def most_frequent_word_in_string(string: str) -> str or None:
    if string is None or len(string) <= 0:
        return None
    str_array = string.split()
    freq = {}
    max_freq = 0
    max_freq_word = ""
    for i in str_array:
        tmp = i.lower()
        if tmp in freq:
            freq[tmp] += 1
        else:
            freq[tmp] = 1
        if freq[tmp] > max_freq:
            max_freq = freq[tmp]
            max_freq_word = tmp
    print(max_freq)
    return max_freq_word


def main():
    string = "Best item in category Lenovo Item Samsung Lenovo > item"
    print(most_frequent_word_in_string(string))


if __name__ == '__main__':
    main()
