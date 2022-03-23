def sortedSquares(nums: list[int]) -> list[int]:
    pos = 0
    while pos < len(nums) and nums[pos] < 0:
        pos += 1
    neg = pos - 1
    res = []
    while 0 <= neg < pos < len(nums):
        sq1 = nums[neg] * nums[neg]
        sq2 = nums[pos] * nums[pos]
        if sq1 < sq2:
            res.append(sq1)
            neg -= 1
        else:
            res.append(sq2)
            pos += 1
    while neg >= 0 and pos >= len(nums):
        sq1 = nums[neg] * nums[neg]
        res.append(sq1)
        neg -= 1

    while neg < 0 and pos < len(nums):
        sq2 = nums[pos] * nums[pos]
        res.append(sq2)
        pos += 1

    return res


def main():
    nums = [-7]
    print(sortedSquares(nums))


if __name__ == '__main__':
    main()
