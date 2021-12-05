from LinkedList_Python.LinkedList import LinkedList


class StackLinkedList:
    def __init__(self):
        self.length = 0
        self.items = LinkedList()

    def push(self, data):
        self.length = self.length + 1
        return self.items.insert(data)

    def pop(self):
        self.length = self.length - 1
        return self.items.deleteLast()

    def top(self):
        return self.items.getLast()

    def printStack(self):
        return self.items.printList()

    def isEmpty(self):
        return self.length == 0


if __name__ == '__main__':
    st = StackLinkedList()
    arr = [1, 2, 3, 4, 5, 6, 7]
    for i in arr:
        st.push(i)
    print(st.pop())
    print(st.top())
    st.printStack()
