from Stack import Stack


def next_larger(arr):
    if len(arr) == 0:
        return None
    st = Stack()
    st.push(arr[0])
    ans = ""
    for idx in range(1, len(arr)):
        if st.isEmpty():
            st.push(arr[idx])
        elif arr[idx] > st.top():
            while not st.isEmpty():
                if arr[idx] > st.top():
                    ans = ans + str(arr[idx]) + " "
                    st.pop()
                else:
                    break
        st.push(arr[idx])
    while not st.isEmpty():
        ans = ans + '-1 '
        st.pop()
    return ans


if __name__ == '__main__':
    arr = [1, 4, 2, 6, 1, 8, 3]
    print(next_larger(arr))
