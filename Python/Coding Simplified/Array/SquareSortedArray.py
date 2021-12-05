def square(num):
    if num is None:
        return None
    return num * num


def square_sorted_array(arr):
    start = 0
    end = len(arr) - 1
    output = []
    for i in arr:
        output.append(i)
    while start <= end:
        if square(arr[start]) > square(arr[end]):
            output[end - start] = square(arr[start])
            start += 1
        else:
            output[end - start] = square(arr[end])
            end -= 1
    return output


def main():
    arr = [-6, -4, -2, 1, 3, 5]
    print(square_sorted_array(arr))


if __name__ == '__main__':
    main()