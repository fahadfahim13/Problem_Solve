class PriorityQueue:
    def __init__(self):
        self.items = []

    def push(self, item):
        if item is None:
            return False
        self.items.append(item)
        if len(self.items) != 1:
            for idx in range(len(self.items) - 1, 0, -1):
                if self.items[idx - 1] < self.items[idx]:
                    tmp = self.items[idx]
                    self.items[idx] = self.items[idx - 1]
                    self.items[idx - 1] = tmp
                else:
                    break
        return True

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop(0)

    def top(self):
        if len(self.items) == 0:
            return None
        return self.items[0]

    def printQ(self):
        print(self.items)


if __name__ == '__main__':
    q = PriorityQueue()
    arr = [1, 2, 6, 3, 0, 7, 9]
    for i in arr:
        q.push(i)

    q.printQ()
    print(q.pop())
    print(q.top())
    q.printQ()
    print(q.pop())
    q.printQ()
