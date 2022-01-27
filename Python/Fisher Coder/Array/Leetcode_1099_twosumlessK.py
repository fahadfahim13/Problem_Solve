def two_sum_less_K(arr: list[int], k: int) -> int:
    numbers = sorted(arr)
    left = 0
    right = len(numbers) - 1
    largest_sum = -1
    while left < right:
        if k > numbers[left] + numbers[right] > largest_sum:
            largest_sum = numbers[left] + numbers[right]
        elif k - numbers[left] < numbers[right]:
            right -= 1
        else:
            left += 1
    return largest_sum


def main():
    arr = [34, 23, 1, 24, 75, 33, 54, 8]
    k = 60
    print(two_sum_less_K(arr, k))


if __name__ == '__main__':
    main()
