def subarray_multiplication_less_than_k(arr: list, k: int) -> list[list]:
    if arr is None or k is None or len(arr) <= 0:
        return []
    current_multiplication = 1
    start = 0
    solution = []
    for i in range(len(arr)):
        current_multiplication = current_multiplication * arr[i]

        while current_multiplication >= k:
            current_multiplication = current_multiplication / arr[start]
            start += 1
        temp_list = []
        for j in range(i, start - 1, -1):
            temp_list.append(arr[j])
            solution.append(temp_list.copy())

    return solution


def main():
    arr = [4, 2, 5, 3, 6]
    print(subarray_multiplication_less_than_k(arr, 10))


if __name__ == '__main__':
    main()
    