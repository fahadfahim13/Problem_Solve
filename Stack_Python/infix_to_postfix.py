from Stack import Stack


def get_priority(ch):
    if ch == '(' or ch == ')':
        return 4
    elif ch == '*' or ch == '/':
        return 3
    elif ch == '+' or ch == '-':
        return 2
    return 1


def infix_to_postfix(string):
    st = Stack()
    postfix = ''
    for i in string:

        if i != '+' and i != '-' and i != '*' and i != '/' and i != '(' and i != ')':
            postfix = postfix + str(i)
        else:
            if st.isEmpty():
                st.push(i)
            elif i == '(':
                st.push(i)
            elif i == ')':
                while not st.isEmpty():
                    itm = st.pop()
                    if itm != '(':
                        postfix = postfix + str(itm)
                    else:
                        break
            else:
                top = st.top()
                if st.isEmpty():
                    st.push(i)
                elif get_priority(i) > get_priority(top):
                    st.push(i)
                elif get_priority(i) <= get_priority(top):
                    while not st.isEmpty() and get_priority(i) <= get_priority(top) and 1 < get_priority(top) < 4:
                        postfix = postfix + str(top)
                        st.pop()
                        top = st.top()
                    st.push(i)

    while not st.isEmpty():
        itm = st.pop()
        postfix = postfix + str(itm)

    return postfix


def postfix_calculation(postfix_string):
    st = Stack()
    for i in postfix_string:
        if i != '+' and i != '-' and i != '*' and i != '/' and i != '(' and i != ')':
            st.push(int(i))
        else:
            a = st.pop()
            b = st.pop()

            if i == '+':
                st.push(int(b+a))
            elif i == '-':
                st.push(int(b - a))
            elif i == '*':
                st.push(int(b * a))
            else:
                st.push(int(b / a))
    return st.top()


if __name__ == '__main__':
    string = "2+3*4"   # 2+3*4, 3*(4+5)-6/(1+2), 3*4+5-6/1+2
    newstr = infix_to_postfix(string)
    print(newstr)
    print(postfix_calculation(newstr))
