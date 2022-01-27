def intersection2(arr1: list[int], arr2: list[int], arr3: list[int]) -> list[int]:
    res = []
    i = 0
    j = 0
    k = 0
    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] and arr1[i] == arr3[k]:
            res.append(arr1[i])
            i += 1
            j += 1
            k += 1
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1
    return res


def intersection(arr1: list[int], arr2: list[int], arr3: list[int]) -> list[int]:
    obj = {}
    for num in arr1:
        if num in obj:
            obj[num] += 1
        else:
            obj[num] = 1
    for num in arr2:
        if num in obj:
            obj[num] += 1
        else:
            obj[num] = 1
    for num in arr3:
        if num in obj:
            obj[num] += 1
        else:
            obj[num] = 1
    res = []
    for key in obj.keys():
        if obj[key] >=3:
            res.append(key)
    return res


def main():
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [1, 2, 5, 7, 9]
    arr3 = [1, 3, 4, 5, 8]
    print(intersection2(arr1, arr2, arr3))


if __name__ == '__main__':
    main()
