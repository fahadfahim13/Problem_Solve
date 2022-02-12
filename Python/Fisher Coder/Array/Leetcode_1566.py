def find_pattern(arr: list[int], m: int, k: int) -> bool:
    for i in range(0, len(arr) - m):
        tmp1 = arr[i:i + m]
        time_count = 1
        print("Tmp1: ", tmp1)
        for j in range(i + m, len(arr), m):
            new_arr = arr[j: j + m]
            print("newArr: ", new_arr)
            if new_arr == tmp1:
                time_count += 1
                if time_count >= k:
                    return True
            else:
                break
    return False


def main():
    # arr = [1, 2, 4, 4, 4, 4]
    arr = [1, 2, 1, 2, 1, 1, 1, 3]
    m = 2
    k = 2
    print(find_pattern(arr, m, k))


if __name__ == '__main__':
    main()
