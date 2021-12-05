def cyclic_sort_array(arr: list) -> list:
    if arr is None or len(arr) <= 0:
        return []
    for i in range(len(arr)):
        j = arr[i] - 1
        if i != j:
            arr[i], arr[j] = arr[j], arr[i]
    return arr


def main():
    arr = [3, 4, 6, 2, 1, 5]
    print(cyclic_sort_array(arr))


if __name__ == '__main__':
    main()
