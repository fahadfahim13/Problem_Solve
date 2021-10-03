from queue import Queue


def max_element_subarray_of_size_k(arr, k):
    if arr is None or len(arr) == 0 or k <= 0:
        return None
    left = 0
    right = 0
    q = []
    q.append(right)
    while right < k:
        if len(q) > 0:
            if arr[q[0]] <= arr[q[right]]:
                q.pop(0)
        q.append(right)
        right += 1

    for i in range(k, len(arr)):
        print(arr[q[0]], end=" ")
        while len(q) > 0 and i - k >= q[0]:
            q.pop(0)
        while len(q) > 0 and arr[q[0]] <= arr[q[i]]:
            q.pop(0)
        q.append(i)


if __name__ == '__main__':
    arr = [2, 5, 4, 3, 1, 7]
    max_element_subarray_of_size_k(arr, 3)