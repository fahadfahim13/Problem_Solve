def twoSum(numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1
    ans_arr = []
    while left < right:
        current = numbers[left] + numbers[right]
        if current == target:
            ans_arr.append(left + 1)
            ans_arr.append(right + 1)
            left += 1
            right -= 1
        elif current < target:
            left += 1
        else:
            right -= 1

    return ans_arr


def twoSum_Prev_solution(numbers: list[int], target: int) -> list[int]:
    arr_map = {}
    for idx, num in enumerate(numbers):
        if num not in arr_map:
            arr_map[num] = [idx]
        else:
            arr_map[num].append(idx)
    ans_list = []
    for el in numbers:
        if target - el in arr_map:
            x = arr_map[el][0]
            y = arr_map[target - el][0]
            if el == target - el:
                if len(arr_map[el]) > 1:
                    y = arr_map[target - el][1]
                else:
                    continue
            arr_map[el].pop(0)
            ans_list.append(x + 1)
            if len(arr_map[el]) == 0:
                arr_map.pop(el)

            arr_map[target - el].pop(0)
            ans_list.append(y + 1)
            if len(arr_map[target - el]) == 0:
                arr_map.pop(target - el)

    return ans_list


def main():
    # numbers = [2, 7, 11, 15]
    numbers = [2, 3, 3, 4]
    target = 6
    print(twoSum(numbers, target))


if __name__ == '__main__':
    main()
