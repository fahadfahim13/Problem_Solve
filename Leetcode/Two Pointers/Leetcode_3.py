def lengthOfLongestSubstring(s: str) -> int:
    if len(s) < 2:
        return len(s)
    l = 0
    r = 0
    max_count = 0
    chars = {}
    while r < len(s):
        if s[r] not in chars:
            chars[s[r]] = r
            r += 1
        else:
            f = chars[s[r]]
            while l <= f:
                if s[l] in chars:
                    del chars[s[l]]
                    l += 1
        max_count = max(max_count, len(chars))
    return max_count


def main():
    s = "dvdf"
    print(lengthOfLongestSubstring(s))


if __name__ == '__main__':
    main()
