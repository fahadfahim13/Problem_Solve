def contain_duplicate(arr: list[int]) -> bool:
    obj = {}
    for num in arr:
        if num in obj:
            return True
        else:
            obj[num] = 1
    return False


def main():
    arr = [1, 2, 3, 4]
    print(contain_duplicate(arr))


if __name__ == '__main__':
    main()
