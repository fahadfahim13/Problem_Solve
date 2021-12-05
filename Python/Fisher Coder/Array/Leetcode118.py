def pascals_triangle_brute_force(num_rows: int) -> list[list[int]] or None:
    if num_rows is None or num_rows <= 0:
        return None
    ans_arr = [[] for i in range(num_rows)]
    for i in range(num_rows):
        for j in range(i + 1):
            if j == 0 or j == i:
                ans_arr[i].append(1)
            elif 0 < j < i:
                ans_arr[i].append(ans_arr[i - 1][j] + ans_arr[i - 1][j - 1])
    return ans_arr


def main():
    num_rows = 5
    print(pascals_triangle_brute_force(num_rows))


if __name__ == '__main__':
    main()
