def union_of_two_sorted_arrays(arr1, arr2):
    if arr1 is None and arr2 is None:
        return None
    numset = set()
    i = 0
    j = 0
    # while i < len(arr1) and j < len(arr2):
    #     if arr1[i] < arr2[j]:
    #         numset.add(arr1[i])
    #         i += 1
    #     else:
    #         numset.add(arr2[j])
    #         j += 1

    while i < len(arr1):
        numset.add(arr1[i])
        i += 1
    while j < len(arr2):
        numset.add(arr2[j])
        j += 1

    return list(numset)


if __name__ == '__main__':
    arr1 = [1, 2, 3, 5, 8, 12]
    arr2 = [3, 5, 7, 8, 10, 11, 14, 15]

    print(union_of_two_sorted_arrays(arr1, arr2))
