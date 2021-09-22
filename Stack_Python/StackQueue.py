from Queue_Python.Queue import QueuePersonal


class StackQueue:
    def __init__(self):
        self.items = QueuePersonal()

    def push(self, item):
        if item is None:
            return False
        return self.items.push(item)

    def pop(self):
        if self.items.isEmpty():
            return None
        q = self.items
        q2 = QueuePersonal()
        while q.length() > 1:
            q2.push(q.pop())
        self.items = q2
        return q.pop()

    def top(self):
        if self.items.isEmpty():
            return None
        q = self.items
        q2 = QueuePersonal()
        while q.length() > 1:
            q2.push(q.pop())
        self.items = q2
        item = q.pop()
        self.items.push(item)
        return item

    def isEmpty(self):
        return self.items.isEmpty()

    def length(self):
        return self.items.length()
