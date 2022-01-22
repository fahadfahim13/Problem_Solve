def shift_grid_k_times(grid: list[list[int]], k: int) -> list[list[int]]:
    ans_arr = grid
    curr_i = 0
    curr_j = 0
    i = 0
    j = 0
    n = len(grid)
    while i < n:
        curr_i = i
        curr_j = j
        while (curr_j + k) > n:
            pass
    return ans_arr
