from collections import deque


def sliding_window_maximum_size_k(arr, k):
    if arr is None or len(arr) <= 0 or k is None:
        return None
    output = []
    q = deque()
    left = 0
    for i in range(0, len(arr)):
        while q and arr[q[-1]] < arr[i]:
            q.pop()
        q.append(i)
        if left > q[0]:
            q.popleft()

        if (i - left) >= k:
            output.append(arr[q[0]])
            left += 1

    return output


if __name__ == '__main__':
    arr = [10, 9, 8, 5, 6, 7, 4, 3, 2, 1]
    print(sliding_window_maximum_size_k(arr, 3))
