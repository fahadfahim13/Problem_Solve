def removeDuplicates(nums: list[int]) -> int:
    if len(nums) <= 2:
        return len(nums)
    id = 2
    for i in range(2, len(nums)):
        if nums[i] != nums[id - 2]:
            nums[id] = nums[i]
            id += 1
    return id


def main():
    nums = [1, 1, 1, 2, 2, 3]
    print(removeDuplicates(nums))


if __name__ == '__main__':
    main()
