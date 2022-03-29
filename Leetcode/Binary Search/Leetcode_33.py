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


def search(nums: list[int], target: int) -> int:
    min_num = findMin(nums)
    n = len(nums)
    left = 0
    right = len(nums) - 1
    if min_num != 0:
        if nums[0] <= target <= nums[min_num - 1]:
            left = 0
            right = min_num - 1
        elif nums[min_num] <= target <= nums[n - 1]:
            left = min_num
            right = n - 1
        else:
            return -1
            

    while left <= right:
        mid = left +(right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1
        


def main():
    nums = [1]
    target = 7
    print(search(nums, target))


if __name__ == '__main__':
    main()


# [3,4,5,6,7,0,1,2]
