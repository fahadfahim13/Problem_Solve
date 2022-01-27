def shift_grid_once(grid: list[list[int]]) -> list[list[int]]:
    flat_arr = []
    m = len(grid)
    n = len(grid[0])
    for arr in grid:
        for num in arr:
            flat_arr.append(num)
    num = flat_arr.pop()
    flat_arr.insert(0, num)
    res_arr = []
    for i in range(0, m):
        temp_arr = []
        for j in range(0, n):
            temp_arr.append(flat_arr.pop(0))
        res_arr.append(temp_arr)
    return res_arr


def shift_grid_k_times(grid: list[list[int]], k: int) -> list[list[int]]:
    m = len(grid)
    n = len(grid[0])
    num_of_shift = k % (m * n)
    res_arr = grid
    for i in range(0, num_of_shift):
        res_arr = shift_grid_once(res_arr)
    return res_arr


def main():
    # grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    grid = [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10]]
    k = 3
    print(shift_grid_k_times(grid, k))


if __name__ == '__main__':
    main()
