def reverse_integer(x: int) -> int:
    r = 2 ** 31
    num = abs(x)
    ans = 0
    while num != 0:
        p = num % 10
        ans = ans * 10 + p
        num = num // 10
    if x < 0:
        ans = -ans
    return ans if abs(ans) <= r - 1 else 0


def main():
    num = 1534236469
    print(reverse_integer(num))


if __name__ == '__main__':
    main()
