def partitionLabels(s: str) -> list[int]:
    last_occurance = {}
    ans = []
    for idx, ch in enumerate(s):
        last_occurance[ch] = idx
    i = 0
    while i < len(s):
        l = last_occurance[s[i]]
        j = i + 1
        while j < l:
            if last_occurance[s[j]] > l:
                l = last_occurance[s[j]]
            j += 1
        ans.append(l - i + 1)
        i = l + 1
    return ans


def main():
    s = "eccbbbbdec"
    print(partitionLabels(s))


if __name__ == '__main__':
    main()
