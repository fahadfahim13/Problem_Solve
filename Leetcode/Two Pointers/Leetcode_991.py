def brokenCalc(startValue: int, target: int) -> int:
    if startValue >= target:
        return startValue - target
    if target % 2 == 0:
        return 1 + brokenCalc(startValue, target // 2)
    return 1 + brokenCalc(startValue, target + 1)


def main():
    startValue = 3
    target = 10
    print(brokenCalc(startValue, target))


if __name__ == '__main__':
    main()
