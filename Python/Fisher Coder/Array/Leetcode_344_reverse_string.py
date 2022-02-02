def reverse_string(s: list[str]):
    l = 0
    r = len(s) - 1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1


def main():
    string = ["h","e","l","l","o"]
    # string = ["H","a","n","n","a","h"]
    reverse_string(string)
    print(string)


if __name__ == '__main__':
    main()
