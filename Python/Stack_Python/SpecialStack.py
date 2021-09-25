import math


class SpecialStack:
    def __init__(self):
        self.items = []
        self.min = math.inf

    def isEmpty(self):
        return len(self.items) == 0

    def top(self):
        if self.isEmpty():
            return None
        return self.items[-1]

    def push(self, item):
        if item is None:
            return False
        if self.isEmpty():
            self.items.append(item)
            self.min = item
        elif item >= self.min:
            self.items.append(item)
        else:
            self.items.append(2*item - self.min)
            self.min = item
        return True

    def pop(self):
        if self.isEmpty():
            return None
        if self.top() < self.min:
            self.min = 2*self.min - self.top()
        return self.items.pop(-1)

    def getMin(self):
        return self.min


if __name__ == '__main__':
    arr = [8, 10, 6, 3, 7, 9]
    st = SpecialStack()
    for i in arr:
        st.push(i)
    print(st.getMin())
    st.pop()
    print(st.getMin())
    st.pop()
    print(st.getMin())
    st.pop()
    print(st.getMin())
    st.pop()
    print(st.getMin())
