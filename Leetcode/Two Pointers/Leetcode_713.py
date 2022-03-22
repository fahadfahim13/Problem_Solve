def numSubarrayProductLessThanK(nums: list[int], k: int) -> int:
    slow = 0
    subarrays = 0
    count = 0
    prod = 1
    for i in range(len(nums)):
        prod *= nums[i]
        subarrays += 1
        while prod >= k and slow <= i:
            prod = prod // nums[slow]
            slow += 1
            subarrays -= 1
        count += subarrays
    return count


def main():
    nums = [10, 5, 2, 6]
    k = 100
    print(numSubarrayProductLessThanK(nums, k))


if __name__ == '__main__':
    main()
