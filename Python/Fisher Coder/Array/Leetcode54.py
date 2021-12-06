def spiralMatrix(nums: list[list[int]]) -> list[int]:
    if nums is None or len(nums) == 0 or len(nums[0]) == 0:
        return []
    n = len(nums[0])
    m = len(nums)
    top = 0
    bottom = m - 1
    left = 0
    right = n - 1
    ans_arr = []

    while len(ans_arr) < m * n:
        for j in range(left, right + 1):
            if len(ans_arr) < m * n:
                ans_arr.append(nums[top][j])
            else:
                break
        top += 1
        for j in range(top, bottom + 1):
            if len(ans_arr) < m * n:
                ans_arr.append(nums[j][right])
            else:
                break
        right -= 1
        for j in range(right, left - 1, -1):
            if len(ans_arr) < m * n:
                ans_arr.append(nums[bottom][j])
            else:
                break
        bottom -= 1

        for j in range(bottom, top - 1, -1):
            if len(ans_arr) < m * n:
                ans_arr.append(nums[j][left])
            else:
                break
        left += 1

    return ans_arr


def main():
    # arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(spiralMatrix(arr))


if __name__ == '__main__':
    main()
