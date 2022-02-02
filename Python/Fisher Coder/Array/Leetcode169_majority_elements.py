def majority_elements(nums: list[int]) -> int:
    count = 1
    res = nums[0]
    for i in range(1, len(nums)):
        if count == 0 and res != nums[i]:
            count = 1
            res = nums[i]
        elif res != nums[i]:
            count -= 1
        elif res == nums[i]:
            count += 1
    return res


def main():
    nums = [3,2,3]
    print(majority_elements(nums))


if __name__ == '__main__':
    main()
