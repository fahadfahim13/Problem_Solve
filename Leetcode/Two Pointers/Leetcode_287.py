class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                return abs(nums[i])
            else:
                nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1]
        return abs(nums[-1])

