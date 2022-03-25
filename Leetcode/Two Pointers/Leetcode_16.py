def threeSumClosest(nums: list[int], target: int) -> int:
    nums = sorted(nums)
    n = len(nums)
    diff = 9999999
    result = 0
    for i in range(0, n - 1):
        j = i + 1
        k = n - 1
        while j < k:
            sum = nums[k] + nums[i] + nums[j]
            if abs(diff) > abs(sum - target):
                diff = abs(sum - target)
                result = sum
            if sum < target:
                j += 1
            else:
                k -= 1
    return result


def main():
    nums = [-1, 2, 1, -4]
    target = 1
    print(threeSumClosest(nums, target))


if __name__ == '__main__':
    main()
