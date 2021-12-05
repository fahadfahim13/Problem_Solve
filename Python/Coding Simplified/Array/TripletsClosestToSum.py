import math


def triplets_closest_to_sum(arr: list, given_sum: int) -> list[tuple]:
    if len(arr) <= 0 or given_sum is None:
        return []
    output = []
    min_diff = math.inf
    arr = sorted(arr)
    for i in range(0, len(arr) - 2):
        start = i + 1
        end = len(arr) - 1
        while start < end:
            temp_sum = (arr[i] + arr[start] + arr[end])
            current_diff = int(math.fabs(temp_sum - given_sum))
            if current_diff < min_diff:
                min_diff = current_diff
                output = [(arr[i], arr[start], arr[end])]
                start += 1
            elif current_diff == min_diff:
                output.append((arr[i], arr[start], arr[end]))
                start += 1
            else:
                end -= 1
    return output


def main():
    arr = [2, -3, 4, 2]
    given_sum = 1
    print(triplets_closest_to_sum(arr, given_sum))


if __name__ == '__main__':
    main()
