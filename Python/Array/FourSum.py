def four_sum(arr, given_sum):
    if arr is None or len(arr) <= 0 or given_sum is None:
        return None
    output = []
    arr = sorted(arr)
    for i in range(0, len(arr) - 3):
        for j in range(i+1, len(arr) - 2):
            start = j + 1
            end = len(arr) - 1
            while start < end:
                if (arr[start] + arr[end] + arr[i] + arr[j]) == given_sum:
                    output.append((arr[start], arr[end], arr[i], arr[j]))
                    start += 1
                    end -= 1
                elif (arr[start] + arr[end] + arr[i] + arr[j]) > given_sum:
                    end -= 1
                else:
                    start += 1
    return output


def main():
    arr = [1, 2, -3, 4, -2, -1, 3]
    print(four_sum(arr, 3))


if __name__ == '__main__':
    main()
