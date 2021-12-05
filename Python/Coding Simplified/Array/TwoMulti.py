def two_multi(arr, num):
    num_set = set()
    for i in arr:
        if int(num/i) in num_set:
            return i, int(num/i)
        num_set.add(i)

    return None


if __name__ == "__main__":
    arr = [4, 1, 3, 10, 7, 5, 8]
    print(two_multi(arr, 21))