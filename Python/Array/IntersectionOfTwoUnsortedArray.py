def intersection_of_two_unsorted_array(arr1, arr2):
    num_set = set()
    ans_set = set()
    for i in arr1:
        num_set.add(i)
    for j in arr2:
        if j in num_set:
            ans_set.add(j)
    return list(ans_set)


if __name__ == '__main__':
    arr1 = [2, 2, 2, 3, 3, 4, 7, 8]
    arr2 = [1, 2, 4, 4, 6, 6, 7, 8, 10]
    print(intersection_of_two_unsorted_array(arr1, arr2))