def minimumLength(s: str) -> int:
    l = 0
    r = len(s) - 1
    while l < r and s[l] == s[r]:
        temp = s[l]
        while l <= r and s[l] == temp:
            l += 1
        while l <= r and s[r] == temp:
            r -= 1
    return r - l + 1 if l <= r else 0


def main():
    s = "aabccabba"
    print(minimumLength(s))


if __name__ == '__main__':
    main()
