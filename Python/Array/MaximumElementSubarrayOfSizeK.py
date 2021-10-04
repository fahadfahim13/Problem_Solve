def max_element_subarray_of_size_k(arr, k):
    if arr is None or len(arr) == 0 or k <= 0:
        return None
    left = 0
    right = 0
    q = [right]
    for i in range(0, k):
        while len(q) > 0 and arr[i] > arr[q[len(q) - 1]]:
            q.pop(len(q) - 1)
        q.append(i)

    for i in range(k, len(arr)):
        print(arr[q[0]], end=" ")
        while len(q) > 0 and i - k >= q[0]:
            q.pop(0)
        while len(q) > 0 and arr[i] > arr[q[len(q) - 1]]:
            q.pop(len(q) - 1)
        q.append(i)

    print(arr[q[0]], end=" ")


if __name__ == '__main__':
    # arr = [2, 5, 4, 3, 1, 7]
    arr = [10, 9, 8, 5, 6, 7, 4, 3, 2, 1]
    max_element_subarray_of_size_k(arr, 3)
