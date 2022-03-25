def maxOperations(nums: list[int], k: int) -> int:
    c_map = {}
    c = 0
    for i in range(len(nums)):
        if k - nums[i] in c_map and c_map[k - nums[i]] > 0:
            c += 1
            c_map[k - nums[i]] -= 1
        else:
            if nums[i] in c_map:
                c_map[nums[i]] += 1
            else:
                c_map[nums[i]] = 1
    return c


def main():
    nums = [1, 2, 3, 4]
    k = 5
    print(maxOperations(nums, k))


if __name__ == '__main__':
    main()
