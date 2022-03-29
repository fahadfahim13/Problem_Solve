def findMin(nums: list[int]) -> int:
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = left +(right - left) // 2
        if mid > 0 and nums[mid] < nums[mid - 1]:
            return mid
        elif nums[mid] >= nums[left] and nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid - 1
    return left


def search(nums: list[int], target: int) -> bool:
    n = len(nums)
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        while left< right and nums[left] == nums[left + 1]:
            left += 1
        while left< right and nums[right] == nums[right - 1]:
            right -= 1
        mid = left +(right - left) // 2
        if nums[mid] == target:
            return True
        if nums[mid] > target:
            if nums[left] <= target and nums[left] < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
                
        else:
            if nums[right] >= target and nums[right] > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
    return False
        


def main():
    nums = [2, 1]
    target = 3
    print(search(nums, target))


if __name__ == '__main__':
    main()


# [3,4,5,6,7,0,1,2]
