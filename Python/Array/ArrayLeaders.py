def array_leaders(arr):
    if arr is None:
        return None
    
    max_till_now = arr[len(arr) - 1]
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] >= max_till_now:
            print(arr[i])
            max_till_now = arr[i]


if __name__ == '__main__':
    arr = [14, 15, 8, 9, 5, 2]
    array_leaders(arr)
