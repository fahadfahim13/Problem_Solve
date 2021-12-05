def reverse_vowels(string: str) -> str or None:
    if string is None or len(string) <= 0:
        return None
    start, end = 0, len(string) - 1
    ans_array = list(string)
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    while start < end:
        if ans_array[start] in vowels and ans_array[end] in vowels:
            ans_array[start], ans_array[end] = ans_array[end], ans_array[start]
            start += 1
            end -= 1
        elif ans_array[start] in vowels:
            end -= 1
        elif ans_array[end] in vowels:
            start += 1
        else:
            start += 1
            end -= 1
    return ''.join(ans_array)


def main():
    string = "educaetion"
    print(reverse_vowels(string))


if __name__ == '__main__':
    main()
