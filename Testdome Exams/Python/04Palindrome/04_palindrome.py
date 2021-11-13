def is_palindrome(word):
    word = word.lower()
    mid = len(word) // 2
    mod = len(word) % 2
    return word[:mid] == word[len(word) - 1:mid + mod -1: -1]


def main():
    print(is_palindrome('Deleveled'))


if __name__ == '__main__':
    main()
