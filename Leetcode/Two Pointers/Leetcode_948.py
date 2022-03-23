def bagOfTokensScore(tokens: list[int], power: int) -> int:
    tokens = sorted(tokens)
    score = 0
    l = 0
    r = len(tokens) - 1
    result = 0
    while l <= r:
        if power >= tokens[l]:
            power -= tokens[l]
            score += 1
            l += 1
            result = max(result, score)
        elif score > 0:
            score -= 1
            power += tokens[r]
            r -= 1
            result = max(result, score)
        else:
            l += 1
            r -= 1
    return result


def main():
    tokens = [100, 200, 300, 400]
    power = 200
    print(bagOfTokensScore(tokens, power))


if __name__ == '__main__':
    main()
