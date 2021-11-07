from queue import PriorityQueue


def kth_smallest_in_array(arr: list[int], k: int) -> int:
    temp_arr = PriorityQueue()
    maxi = max(arr)
    kth_smallest = 0
    for i in range(k):
        temp_arr.put((maxi - arr[i], arr[i]))
    kth_smallest = temp_arr.get()
    temp_arr.put(kth_smallest)
    kth_smallest = kth_smallest[1]
    for i in range(k, len(arr)):
        if arr[i] < kth_smallest:
            temp_arr.get()
            temp_arr.put((maxi - arr[i], arr[i]))
            kth_smallest = temp_arr.get()
            temp_arr.put(kth_smallest)
            kth_smallest = kth_smallest[1]

    return kth_smallest


def main():
    arr = [10, 7, 11, 30, 20, 38, 2, 45]
    k = 7
    print(kth_smallest_in_array(arr, k))


if __name__ == '__main__':
    main()
