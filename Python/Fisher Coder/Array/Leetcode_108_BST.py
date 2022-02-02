class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBst(self, nums, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        node = TreeNode(nums[mid], self.createBst(nums, start, mid - 1), self.createBst(nums, mid + 1, end))
        return node

    def sortedArrayToBST(self, nums: list[int]):
        return self.createBst(nums, 0, len(nums) - 1)


def main():
    nums = [-10, -3, 0, 5, 9]
    s = Solution()
    print(s.sortedArrayToBST(nums))


if __name__ == '__main__':
    main()
