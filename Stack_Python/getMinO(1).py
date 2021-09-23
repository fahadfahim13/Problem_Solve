from Stack import Stack


def sortArray(arr):
    if arr is None:
        return None
    if len(arr) == 0:
        return None
    st1 = Stack()
    st2 = Stack()
    for i in arr:
        if st1.isEmpty():
            st1.push(i)
        else:
            top = st1.top()
            if i <= top:
                st1.push(i)
            else:
                while i > top:
                    st2.push(st1.pop())
                    if st1.isEmpty():
                        st1.push(i)
                        break
                    top = st1.top()
                while not st2.isEmpty():
                    st1.push(st2.pop())
    return st1


if __name__ == '__main__':
    arr = [7, 8, 3, 1, 5, 9]
    print(sortArray(arr).items)
