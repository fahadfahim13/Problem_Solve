def game_of_life(board: list[list[int]]):
    m = len(board)
    n = len(board[0])
    temp = []
    for i in range(m):
        t = []
        for j in range(n):
            t.append(board[i][j])
        temp.append(t)
    directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    for i in range(m):
        for j in range(n):
            total_live = 0
            for dir in directions:
                x = dir[0] + i
                y = dir[1] + j
                if 0 <= x < m and 0 <= y < n and temp[x][y] == 1:
                    total_live += 1
            if temp[i][j] == 1:
                if total_live < 2:
                    board[i][j] = 0
                elif total_live > 3:
                    board[i][j] = 0
            else:
                if total_live == 3:
                    board[i][j] = 1


def main():
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    board = [[1,1],[1,0]]
    game_of_life(board)
    print(board)


if __name__ == '__main__':
    main()
