def find_duplicates(nums: list[int]) -> list[int]:
    # ans = set()
    ans = []
    for idx, num in enumerate(nums):
        if nums[abs(num) - 1] < 0:
            ans.append(abs(num))
        else:
            nums[abs(num) - 1] = -nums[abs(num) - 1]
    return ans


def main():
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(find_duplicates(nums))


if __name__ == '__main__':
    main()
