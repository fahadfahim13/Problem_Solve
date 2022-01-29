def plus_one(nums: list[int]) -> str:
    ans_list = list(reversed(nums))
    for idx, num in enumerate(ans_list):
        ans_list[idx] = (num + 1) % 10
        if ans_list[idx] != 0:
            break
    if ans_list[-1] == 0:
        ans_list.append(1)
    ans = ''
    for num in reversed(ans_list):
        ans = ans + str(num)
    return ans


def main():
    nums = [9, 9, 9, 9]
    # nums = [1, 2, 3, 4]
    print(plus_one(nums))


if __name__ == '__main__':
    main()
