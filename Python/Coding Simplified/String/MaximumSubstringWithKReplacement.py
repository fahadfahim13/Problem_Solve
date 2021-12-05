import math


def maximum_sub_string_k_replacement(string: str, k: int) -> str or None:
    if string is None or k is None or len(string) <= 0 or k <= 0:
        return None
    max_freq = - math.inf
    freq = {}
    max_len, start, end = 0, 0, 0
    ans_start, ans_end = 0, 0
    while start <= end < len(string):
        if string[end] in freq:
            freq[string[end]] += 1
        else:
            freq[string[end]] = 1
        max_freq = max(max_freq, freq[string[end]])
        if end - start + 1 - max_freq > k:
            freq[string[start]] -= 1
            if freq[string[start]] == 0:
                del freq[string[start]]
            start += 1
        if end - start + 1 > max_len:
            max_len = end - start + 1
            ans_start = start
            ans_end = end
        end += 1
    return max_len


def main():
    string = "bccbababd"
    print(maximum_sub_string_k_replacement(string, 2))


if __name__ == '__main__':
    main()
