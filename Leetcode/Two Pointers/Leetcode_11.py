def maxArea(height: list[int]) -> int:
    left = 0
    right = len(height) - 1
    max_area = -1
    while left <= right:
        area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area


def main():
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(maxArea(height))


if __name__ == '__main__':
    main()
