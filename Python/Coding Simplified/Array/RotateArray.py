from queue import Queue


def rotate_array(arr: list[int], n) -> list[int] or None:
    if arr is None or len(arr) == 0:
        return None
    q = Queue()
    for i in arr:
        q.put(i)

    for i in range(0, n):
        temp = q.get()
        q.put(temp)

    ans_arr = []
    while not q.empty():
        ans_arr.append(q.get())

    return ans_arr


def main():
    arr = [1, 2, 3, 4, 5]
    print(rotate_array(arr, 3))


if __name__ == "__main__":
    main()
