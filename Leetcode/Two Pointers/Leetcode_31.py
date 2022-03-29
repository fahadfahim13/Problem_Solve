def nextPermutation(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # Find the pivot
    pivot = 0
    for i in range(len(nums)-1, 0, -1):
        if nums[i-1] < nums[i]:
            pivot = i
            break
    if pivot == 0:
        nums.sort()
        return
    # Find number that is just big than pivot in the right of the pivot.
    just_bigger = len(nums) - 1
    while nums[just_bigger] <= nums[pivot-1]:
        just_bigger -= 1
    # Swap pivot and just_bigger
    nums[pivot-1], nums[just_bigger] = nums[just_bigger], nums[pivot-1]
    i = pivot
    j = len(nums) - 1
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
        
            


def main():
    nums = [1, 2]
    nextPermutation(nums)
    print(nums)


if __name__ == '__main__':
    main()

    
