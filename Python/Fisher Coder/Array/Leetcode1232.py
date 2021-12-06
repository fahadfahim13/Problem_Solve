def checkStraightLine(coordinates: list[list[int]]) -> bool:
    if coordinates is None:
        return False
    if len(coordinates) < 3:
        return True
    for i in range(1, len(coordinates) - 1):
        slope1 = (coordinates[i + 1][1] - coordinates[0][1]) * (coordinates[i][0] - coordinates[0][0])
        slope2 = (coordinates[i][1] - coordinates[0][1]) * (coordinates[i + 1][0] - coordinates[0][0])
        if slope1 != slope2:
            return False
    return True


def main():
    # coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
    coordinates = [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]
    print(checkStraightLine(coordinates))


if __name__ == '__main__':
    main()
