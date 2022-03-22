def firstPalindrome(words: list[str]) -> str:
    for word in words:
        l = len(word)
        st = 0
        end = l - 1
        while st <= end and word[st] == word[end]:
            st += 1
            end -= 1
        if st > end:
            return word
    return ""


def main():
    words = ["def","ghi"]
    print(firstPalindrome(words))


if __name__ == '__main__':
    main()
