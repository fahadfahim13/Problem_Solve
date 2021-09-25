from LinkedList_Python.LinkedList import LinkedList


class QueueLinkedList:
    def __init__(self):
        self.items = LinkedList()

    def isEmpty(self):
        return self.items.getLength()

    def front(self):
        if self.items.getLength() == 0:
            return None
        return self.items.head.data

    def enqueue(self, item):
        return self.items.insert(item)

    def dequeue(self):
        if self.items.getLength() == 0:
            return None
        return self.items.deleteFirst()

    def printQueue(self):
        self.items.printList()


if __name__ == '__main__':
    q = QueueLinkedList()
    arr = [1, 2, 6, 3, 0, 7, 9]
    for i in arr:
        q.enqueue(i)

    q.printQueue()
    tmp = q.dequeue()
    print()
    print(tmp)
    q.printQueue()
    tmp = q.dequeue()
    print()
    print(tmp)
    q.printQueue()
    tmp = q.dequeue()
    print()
    print(tmp)
    q.printQueue()
    tmp = q.dequeue()
    print()
    print(tmp)
    q.printQueue()
    print()
    print(q.front())
