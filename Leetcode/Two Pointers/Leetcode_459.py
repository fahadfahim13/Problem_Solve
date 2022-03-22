def repeatedSubstringPattern(s: str) -> bool:
    l = len(s) // 2
    print(l)
    for i in range(l, 0, -1):
        j = 0
        if len(s) % i == 0:
            while i + j < len(s) and s[j] == s[j + i]:
                j += 1
            if i + j == len(s):
                return True
    return False


def main():
    s = "aabaaba"
    print(repeatedSubstringPattern(s))


if __name__ == '__main__':
    main()
