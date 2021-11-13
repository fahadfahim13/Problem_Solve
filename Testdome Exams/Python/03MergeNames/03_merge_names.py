from itertools import chain


def unique_names(names1, names2):
    ans = set()
    for i in names1:
        ans.add(i)
    for j in names2:
        ans.add(j)
    return sorted(list(ans))
    # return sorted(list(set(chain(names1, names2))))


def main():
    names1 = ["Olivia", "Ava", "Emma"]
    names2 = ["Olivia", "Sophia", "Emma"]
    print(unique_names(names1, names2))
    # should print Ava, Emma, Olivia, Sophia


if __name__ == '__main__':
    main()
