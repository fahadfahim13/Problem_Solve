from bisect import bisect_left


def binary_search(nums: list[int], target: int) -> int or None:
    left = 0
    right = len(nums) - 1
    mid = (left + right) // 2

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


def majority_number(nums: list[int], target: int) -> bool:
    first_occur = binary_search(nums, target)
    if nums[first_occur] is None:
        return False
    else:
        final_occur = first_occur + len(nums) // 2 - 1
        if final_occur < len(nums) and nums[final_occur] == target:
            return True


def main():
    # arr = [2, 4, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6]
    arr = [10, 100, 101, 101]
    target = 101
    print(majority_number(arr, target))


if __name__ == '__main__':
    main()
