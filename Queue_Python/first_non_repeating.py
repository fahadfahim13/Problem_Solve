from Queue import QueuePersonal


def first_non_repeating(string_inp: str) -> str:
    if string_inp == '':
        return ''
    str_map = {}
    q = QueuePersonal()
    last_repeating = string_inp[0]
    ans_str = ""

    for i in string_inp:
        if i in str_map:
            str_map[i] = str_map[i] + 1
            if i == last_repeating:
                ans_str += "-1"
            else:
                ans_str = ans_str + last_repeating
        else:
            str_map[i] = 1
            if str_map[last_repeating] > 1:
                last_repeating = i
            ans_str = ans_str + last_repeating
            q.push(i)
    return ans_str


if __name__ == '__main__':
    string = "aabbbcddddddce"
    print(first_non_repeating(string))