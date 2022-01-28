def contain_duplicate(nums: list[int], k: int) -> bool:
    obj = {}
    for idx, num in enumerate(nums):
        if num not in obj:
            obj[num] = idx
        else:
            if abs(obj[num] - idx) <= k:
                return True
            else:
                obj[num] = idx
    return False


def main():
    arr = [1,2,3,1,2,3]
    k = 2
    print(contain_duplicate(arr, k))


if __name__ == '__main__':
    main()
