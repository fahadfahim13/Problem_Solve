import random


def shuffle_array(arr):
    output = []
    for i in range(0, len(arr)):
        idx = random.randint(0, len(arr) - 1)
        arr[idx], arr[i] = arr[i], arr[idx]


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    # print(shuffle_array(arr))
    random.shuffle(arr)
    print(arr)
    shuffle_array(arr)
    print(arr)
