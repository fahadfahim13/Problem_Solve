def climbStairs(n: int) -> int:
    dp = [1, 2]
    for i in range(2, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    return dp[n - 1]


def main():
    n = 38
    print(climbStairs(n))


if __name__ == '__main__':
    main()
