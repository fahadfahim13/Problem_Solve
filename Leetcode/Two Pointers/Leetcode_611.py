def triangleNumber(nums: list[int]) -> int:
    nums = sorted(nums)
    c = 0
    k = len(nums) - 1
    while k > 1:
        i = 0
        j = k - 1
        while j > i:
            if nums[i] + nums[j] > nums[k]:
                c += j - i
                j -= 1
            else:
                i += 1
        k -= 1
    return c


def main():
    nums = [2, 2, 3, 4]
    print(triangleNumber(nums))


if __name__ == '__main__':
    main()
