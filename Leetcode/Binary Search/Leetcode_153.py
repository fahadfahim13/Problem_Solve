def findMin(nums: list[int]) -> int:
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2
        if mid > 0 and nums[mid] < nums[mid - 1]:
            return nums[mid]
        elif nums[left] <= nums[mid] and nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid - 1
    return nums[left]

def main():
    nums = [8,9,10,1,2,3,4,5,6,7]
    print(findMin(nums))


if __name__ == '__main__':
    main()

    
# [8,9,10,1,2,3,4,5,6,7]
