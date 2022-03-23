def isPalindrome(s: str, st_id: int, end_id: int) -> bool:
    while st_id <= end_id:
        if s[st_id] != s[end_id]:
            return False
        st_id += 1
        end_id -= 1
    return True


def checkStrings(a: str, b: str) -> bool:
    start = 0
    end = len(b) - 1
    while start <= end and (a[start] == b[end]):
        start += 1
        end -= 1
    if isPalindrome(a, start, end) or isPalindrome(b, start, end):
        return True
    return False


def checkPalindromeFormation(a: str, b: str) -> bool:
    return checkStrings(a, b) or checkStrings(b, a)


def main():
    a = "x"
    b = "y"
    print(checkPalindromeFormation(a, b))


if __name__ == '__main__':
    main()
