from DoublyLinkedList.DoublyLinkedList import DoublyLinkedList


class LRUQueue:
    def __init__(self):
        self.items = DoublyLinkedList()
        self.max_nodes = 5
        self.total_nodes = 0

    def push(self, data):
        temp = self.items.delete(data)
        if temp:
            self.total_nodes = self.total_nodes - 1
        if self.total_nodes == self.max_nodes:
            self.pop()
        else:
            self.total_nodes = self.total_nodes + 1
        return self.items.insert(data)

    def pop(self):
        if self.total_nodes > 0:
            self.total_nodes = self.total_nodes - 1
            return self.items.deleteFirst()
        return None

    def top(self):
        return self.items.getFirst()

    def isEmpty(self):
        return self.items.isEmpty()

    def printQ(self):
        return self.items.printLinkedList()


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 6]
    q = LRUQueue()
    for i in arr:
        q.push(i)
    q.printQ()
    print(q.pop().value)
    q.printQ()
    q.push(3)
    q.printQ()
    q.push(4)
    q.printQ()
