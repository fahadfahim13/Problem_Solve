def reverse(arr: list[int], start: int, end: int):
    while start < end < len(arr):
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    # return arr


def rotate_reverse(nums: list[int], k: int) -> list[int]:
    k %= len(nums)
    reverse(nums, 0, len(nums) - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, len(nums) - 1)
    return nums


def rotate(nums: list[int], k: int) -> list[int]:
    p = len(nums) - 1
    for i in range(k):
        num = nums.pop(p)
        nums.insert(0, num)
    return nums


def main():
    arr = [-1]
    k = 2
    print(rotate_reverse(arr, k))


if __name__ == '__main__':
    main()
