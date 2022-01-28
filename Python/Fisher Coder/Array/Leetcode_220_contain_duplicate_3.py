from bisect import bisect_left, bisect_right
from sortedcontainers import SortedList


def contain_duplicate(nums: list[int], k: int, t: int) -> bool:
    obj = SortedList()
    for idx, num in enumerate(nums):
        if idx > k:
            obj.remove(nums[idx - k - 1])
        left_pos = bisect_left(obj, num - t)
        right_pos = bisect_right(obj, num + t)
        if left_pos != right_pos:
            return True
        obj.add(num)
    return False


def main():
    arr = [7,2,8]
    k = 2
    t = 1
    print(contain_duplicate(arr, k, t))


if __name__ == '__main__':
    main()
