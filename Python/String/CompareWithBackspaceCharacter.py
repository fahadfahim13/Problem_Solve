def compare_with_backspace_character(string1: str, string2: str) -> bool or None:
    if string1 is None or string2 is None:
        return False
    modified_string1 = []
    modified_string2 = []
    for i in range(len(string1)):
        if string1[i] != '#':
            modified_string1.append(string1[i])
        else:
            modified_string1.pop()
    for j in range(len(string2)):
        if string2[j] != '#':
            modified_string2.append(string2[j])
        else:
            modified_string2.pop()
    output_string1 = ''.join(modified_string1)
    output_string2 = ''.join(modified_string2)

    return output_string1 == output_string2


def main():
    string1 = "bda##c"
    string2 = "bd#c"
    print(compare_with_backspace_character(string1, string2))


if __name__ == '__main__':
    main()

