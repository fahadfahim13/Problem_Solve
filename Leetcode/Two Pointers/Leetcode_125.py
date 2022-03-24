def isPalindrome(s: str) -> bool:
    temp = ""
    for chr in s:
        if chr.isalnum():
            temp += chr.lower()
    l = 0
    r = len(temp) - 1
    if temp == "":
        return True
    while l <= r:
        if temp[l] != temp[r]:
            return False
        l += 1
        r -= 1
    return True


def main():
    s = " "
    print(isPalindrome(s))


if __name__ == '__main__':
    main()
