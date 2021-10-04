def triplet_less_than_target(arr: list, given_sum: int) -> list[tuple]:
    if arr is None or len(arr) <= 0 or given_sum is None:
        return []
    arr = sorted(arr)
    output = []
    count = 0
    for i in range(0, len(arr) - 2):
        if arr[i] >= given_sum:
            break
        start = i + 1
        end = len(arr) - 1
        while start < end:
            if (arr[start] + arr[end] + arr[i]) < given_sum:
                for num in arr[start+1: end+1]:
                    count += 1
                    output.append((arr[i], arr[start], num))
                start += 1
            else:
                end -= 1
    print(count)
    return output


def main():
    arr = [1, 2, -3, 4, -2]
    print(sorted(arr))
    print(triplet_less_than_target(arr, 1))


if __name__ == '__main__':
    main()