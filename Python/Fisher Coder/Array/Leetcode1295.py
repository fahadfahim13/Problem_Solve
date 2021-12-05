def findNumbersWithEvenDigits(arr: list[int]) -> int:
    count = 0
    for num in arr:
        if len(str(num)) % 2 == 0:
            count += 1
    return count


def main():
    arr = [12, 345, 2, 6, 7896, 299567]
    # arr = [555, 901, 482, 1771]
    print(findNumbersWithEvenDigits(arr))


if __name__ == '__main__':
    main()
