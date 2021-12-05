def intersection_of_two_sorted_arrays(arr1, arr2):
    if arr1 is None and arr2 is None:
        return None
    numset = set()
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            numset.add(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    return list(numset)


if __name__ == '__main__':
    arr1 = [2, 2, 2, 3, 3, 4, 7, 8]
    arr2 = [1, 2, 4, 4, 6, 6, 7, 8, 10]
    print(intersection_of_two_sorted_arrays(arr1, arr2))