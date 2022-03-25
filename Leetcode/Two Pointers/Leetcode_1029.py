def twoCitySchedCost(costs: list[list[int]]) -> int:
    costs = sorted(costs, key=lambda x: x[0] - x[1])
    c = 0
    for i in range(len(costs) // 2):
        c += costs[i][0]

    for i in range(len(costs) // 2, len(costs)):
        c += costs[i][1]

    return c


def main():
    costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
    print(twoCitySchedCost(costs))


if __name__ == '__main__':
    main()
