def move_zeros(nums: list[int]) -> None:
    left = 0
    right = 0
    while left <= right < len(nums):
        if nums[right] != 0:
            if nums[left] == 0:
                nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1


def main():
    arr = [0, 0, 1]
    # arr = [1, 0, 1]
    move_zeros(arr)
    print(arr)


if __name__ == '__main__':
    main()
