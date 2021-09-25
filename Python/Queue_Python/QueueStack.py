from Stack_Python.Stack import Stack


class QueueStack:
    def __init__(self):
        self.items = Stack()
        self.total = 0

    def push(self, data):
        if data is None:
            return False

        if self.total == 0:
            self.items.push(data)
            self.total = self.total + 1
        else:
            temp = Stack()
            while not self.items.isEmpty():
                temp.push(self.items.pop())
            self.items.push(data)
            while not temp.isEmpty():
                self.items.push(temp.pop())
        return True

    def pop(self):
        if self.total == 0:
            return None
        return self.items.pop()

    def top(self):
        if self.total == 0:
            return None
        self.total = self.total - 1
        return self.items.top()

    def isEmpty(self):
        return self.items == 0

    def printQue(self):
        print(self.items.items[::-1])


if __name__ == '__main__':
    arr = [1, 4, 2, 7, 3, 9, 5]
    q = QueueStack()
    for i in arr:
        q.push(i)
    print(q.pop())
    q.printQue()
    print(q.pop())
    q.printQue()
    print(q.pop())
    q.printQue()
    print(q.top())
    q.printQue()
