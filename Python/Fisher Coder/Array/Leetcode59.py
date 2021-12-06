def generateSpiralMatrix(n: int) -> list[list[int]]:
    if n <= 0:
        return [[]]
    current = 1
    left = 0
    right = n - 1
    top = 0
    bottom = n - 1
    ans_arr = [[0 for i in range(n)] for j in range(n)]
    while left <= right and top <= bottom:
        for i in range(left, right + 1):
            ans_arr[top][i] = current
            current += 1
        top += 1
        for j in range(top, bottom + 1):
            ans_arr[j][right] = current
            current += 1
        right -= 1
        for k in range(right, left - 1, -1):
            ans_arr[bottom][k] = current
            current += 1
        bottom -= 1
        for l in range(bottom, top - 1, -1):
            ans_arr[l][left] = current
            current += 1
        left += 1
    return ans_arr


def main():
    n = 4
    print(generateSpiralMatrix(n))


if __name__ == '__main__':
    main()
