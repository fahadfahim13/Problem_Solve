def get_winner(arr: list[int], k: int) -> int:
    winning_streak = 0
    winner = arr[0]
    if k >= len(arr):
        return max(arr)
    for i in range(1, len(arr)):
        if arr[i] > winner:
            winning_streak = 1
            winner = arr[i]
        else:
            winning_streak += 1
        if winning_streak >= k:
            return winner
    return winner
    # while winning_streak < k:
    #     if arr[0] > arr[1]:
    #         if winner == arr[0]:
    #             winning_streak += 1
    #         else:
    #             winning_streak = 1
    #             winner = arr[0]
    #         tmp = arr.pop(1)
    #         arr.append(tmp)
    #     else:
    #         if winner == arr[1]:
    #             winning_streak += 1
    #         else:
    #             winning_streak = 1
    #             winner = arr[1]
    #         tmp = arr.pop(0)
    #         arr.append(tmp)
    # return winner


def main():
    # arr = [2, 1, 3, 5, 4, 6, 7]
    arr = [3, 2, 1]
    k = 2
    print(get_winner(arr, k))


if __name__ == '__main__':
    main()
