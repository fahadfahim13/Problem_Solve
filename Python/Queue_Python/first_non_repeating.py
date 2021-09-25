from Queue import QueuePersonal


def first_non_repeating(string_inp: str) -> str:
    if string_inp == '':
        return ''
    count = {}
    q = QueuePersonal()
    last_repeating = string_inp[0]
    ans_str = ""

    for i in string_inp:
        if i not in count:
            count[i] = 1
            q.push(i)
        else:
            count[i] = count[i] + 1

        while not q.isEmpty():
            temp = q.top()
            if count[temp] == 1:
                ans_str += temp
                break
            q.pop()
        if q.isEmpty():
            ans_str += "X"

    return ans_str


if __name__ == '__main__':
    string = "aabccdba"
    # string = "aba"
    print(first_non_repeating(string))