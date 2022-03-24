def numRescueBoats(people: list[int], limit: int) -> int:
    people = sorted(people)
    l = 0
    r = len(people) - 1
    count = 0
    while l <= r:
        if people[l] + people[r] <= limit:
            l += 1
        r -= 1
        count += 1
    return count


def main():
    people = [3, 5, 3, 4]
    limit = 5
    print(numRescueBoats(people, limit))


if __name__ == '__main__':
    main()
