def numEquivDominoPairs(dominoes: list[list[int]]) -> int:
    count = 0
    domino_map = dict()
    for idx, dom in enumerate(dominoes):
        if (dom[0], dom[1]) not in domino_map:
            if (dom[1], dom[0]) not in domino_map:
                domino_map[(dom[0], dom[1])] = 1
            else:
                domino_map[(dom[1], dom[0])] += 1
        else:
            domino_map[(dom[0], dom[1])] += 1
    print(domino_map)
    for val in domino_map.values():
        if val > 1:
            count += (val - 1) * val // 2
    return count


def main():
    dominoes = [[1, 2], [2, 1], [2, 1], [3, 4], [5, 6]]
    print(numEquivDominoPairs(dominoes))


if __name__ == '__main__':
    main()
