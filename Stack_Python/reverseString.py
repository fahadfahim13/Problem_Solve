from Stack import Stack


def reverseString(string):
    st = Stack()
    for i in string:
        st.push(i)
    newstr = ''
    while not st.isEmpty():
        newstr = newstr + str(st.pop())
    return newstr


def checkCorrectDelimeter(string):
    st = Stack()
    for i in string:
        if i == '(' or i == '{' or i == '[':
            st.push(i)
        elif i == ')':
            popped = st.pop()
            if popped is None or popped != '(':
               return False
        elif i == '}':
            popped = st.pop()
            if popped is None or popped != '{':
               return False
        elif i == ']':
            popped = st.pop()
            if popped is None or popped != '[':
               return False
    return st.isEmpty()


if __name__ == '__main__':
    string = "abcdefg fjglkfdgl"
    print(reverseString(string))
    expr = "[a(b+(c*(u + r))) - {g (a + b)}]"
    print(checkCorrectDelimeter(expr))
