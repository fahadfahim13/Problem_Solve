def remove_duplicates_from_array(arr):
    freq = {}
    res_set = set()
    output = []
    for i in arr:
        res_set.add(i)
        if i not in freq:
            output.append(i)
            freq[i] = 1

    print(output)
    print(list(res_set))


def main():
    arr = [1, 4, 4, 4, 5, 6, 7, 7, 8]
    remove_duplicates_from_array(arr)


if __name__ == '__main__':
    main()
