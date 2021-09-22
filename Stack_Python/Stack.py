class Stack:
    def __init__(self):
        self.length = 0
        self.items = []

    def push(self, item):
        self.items.append(item)
        self.length = self.length + 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        self.length = self.length - 1
        return self.items.pop(-1)

    def top(self):
        if self.length == 0:
            return None
        return self.items[self.length - 1]

    def isEmpty(self):
        return self.length == 0


if __name__ == '__main__':
    st = Stack()
    arr = [1, 2, 3, 4, 5, 6, 7]
    for i in arr:
        st.push(i)

    print(st.pop())
    print(st.pop())
    print(st.top())
    print(st.items)
