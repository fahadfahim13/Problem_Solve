from collections import Counter


def doubled_pairs(nums: list[int]) -> bool:
    count = Counter(nums)
    keys = sorted(nums, key=lambda x: abs(x))
    print(count, keys)
    for num in keys:
        if count[num] == 0:
            continue
        elif count[2 * num] == 0:
            return False
        else:
            count[num] -= 1
            count[2 * num] -= 1
    return True


def main():
    arr = [4, -2, 2, -4]
    print(doubled_pairs(arr))


if __name__ == '__main__':
    main()
