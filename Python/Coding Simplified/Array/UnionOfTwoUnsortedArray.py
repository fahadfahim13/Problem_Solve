def union_of_two_unsorted_array(arr1, arr2):
    numset = set()
    i = 0
    j = 0

    while i < len(arr1):
        numset.add(arr1[i])
        i += 1
    while j < len(arr2):
        numset.add(arr2[j])
        j += 1

    return list(numset)


if __name__ == '__main__':
    arr1 = [21, 22, 12, 3, 15, 14, 7, 8]
    arr2 = [10, 12, 14, 4, 6, 6, 7, 8, 10]
    print(union_of_two_unsorted_array(arr1, arr2))