class QueuePersonal:
    def __init__(self):
        self.items = []

    def push(self, item):
        if item is None:
            return False
        self.items.append(item)
        return True

    def top(self):
        if len(self.items) == 0:
            return None
        return self.items[0]

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop(0)

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        return False

    def length(self):
        return len(self.items)


if __name__ == '__main__':
    q = QueuePersonal()
    arr = [1, 2]
    for i in arr:
        q.push(i)
    print(q.pop())
    print(q.pop())
    print(q.top())
    print(q.items)
