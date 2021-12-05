def check_path(maze: list[list[int]], current: tuple[int, int]) -> bool:
    if 0 <= current[0] <= len(maze) - 1 and 0 <= current[1] <= len(maze) - 1 and maze[current[0]][current[1]]:
        return True
    return False


def find_path(maze: list[list[int]], sol: list[list[int]], current: tuple[int, int]) -> bool:
    if current[0] == len(maze) - 1 and current[1] == len(maze) - 1 and maze[-1][-1]:
        return True
    if check_path(maze, current):
        sol[current[0]][current[1]] = 1
        if find_path(maze, sol, (current[0] + 1, current[1])):
            return True
        if find_path(maze, sol, (current[0], current[1] + 1)):
            return True
        sol[current[0]][current[1]] = 0
    return False


def rat_maze_path(maze: list[list[int]]) -> bool:
    if maze is None:
        return False
    ans_matrix = [[0 for i in range(len(maze))] for j in range(len(maze))]
    current = (0, 0)
    return find_path(maze, ans_matrix, current)


def main():
    # maze = [[1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 1, 1], [0, 0, 0, 1]]
    maze = [[1, 0, 0, 0], [1, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1]]
    print(rat_maze_path(maze))


if __name__ == '__main__':
    main()
