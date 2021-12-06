def getRow(rowIndex: int) -> list[int]:
    if rowIndex < 0:
        return []
    ans = [1]
    for i in range(1, rowIndex + 1):
        ans.append(ans[i - 1] * (rowIndex - i + 1) // i)
    return ans


def main():
    row_index = 7
    print(getRow(row_index))


if __name__ == '__main__':
    main()
