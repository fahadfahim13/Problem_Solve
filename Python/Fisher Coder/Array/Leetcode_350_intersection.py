def intersection_sorted(nums1: list[int], nums2: list[int]) -> list[int]:
    nums1 = sorted(nums1)
    nums2 = sorted(nums2)
    i = 0
    j = 0
    res = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            res.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    return res


def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    map1 = {}
    map2 = {}
    for idx, num in enumerate(nums1):
        if num not in map1:
            map1[num] = 1
        else:
            map1[num] += 1
    for idx, num in enumerate(nums2):
        if num not in map2:
            map2[num] = 1
        else:
            map2[num] += 1
    map3 = {}
    short_map = map1
    long_map = map2
    if len(map1.keys()) > len(map2.keys()):
        short_map = map2
        long_map = map1
    for key in short_map.keys():
        if key in long_map:
            k = min(short_map[key], long_map[key])
            map3[key] = k
    res = []
    for key in map3.keys():
        num = map3[key]
        for i in range(num):
            res.append(key)
    return res


def main():
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(intersection_sorted(nums1, nums2))


if __name__ == '__main__':
    main()
