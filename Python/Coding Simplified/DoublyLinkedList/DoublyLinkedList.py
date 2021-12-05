from Binary_Tree_Python.Node import LinkedNode


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.total_nodes = 0

    def isEmpty(self):
        return self.total_nodes == 0

    def insert(self, data):
        if data is None:
            return False

        node = LinkedNode(data)
        if self.total_nodes == 0:
            self.head = node
            self.tail = self.head
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.total_nodes = self.total_nodes + 1
        return True

    def insertFirst(self, data):
        if data is None:
            return False
        node = LinkedNode(data)
        if self.total_nodes == 0:
            self.head = node
            self.tail = self.head
        else:
            node.next = self.head
            self.head = node
        self.total_nodes = self.total_nodes + 1
        return True

    def deleteLast(self):
        if self.total_nodes == 0:
            return None
        temp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        return temp

    def deleteFirst(self):
        if self.total_nodes == 0:
            return None
        temp = self.head
        self.head = self.head.next
        self.head.prev = None
        return temp

    def getFirst(self):
        if self.total_nodes == 0:
            return None
        return self.head.value

    def getLast(self):
        if self.total_nodes == 0:
            return None
        return self.tail.value

    def delete(self, item):
        if item is None:
            return False
        if self.total_nodes == 0:
            return False
        node = self.head
        while node is not None:
            if node.value == item:
                if node.prev is not None:
                    node.prev.next = node.next
                    if node.next is not None:
                        node.next.prev = node.prev
                    else:
                        self.tail = self.tail.prev
                else:
                    if node.next is not None:
                        node.next.prev = None
                        self.head = self.head.next
                    else:
                        self.head = None
                        self.tail = None
                self.total_nodes = self.total_nodes - 1
                return True
            node = node.next
        return False

    def printLinkedList(self):
        if self.total_nodes == 0:
            print('No Nodes')
            return False
        node = self.head
        while node is not None:
            print(node.value, end=" ")
            node = node.next
        print()
        return True

    def printReverse(self):
        if self.total_nodes == 0:
            print('No Nodes')
            return False
        node = self.tail
        while node is not None:
            print(node.value, end=" ")
            node = node.prev
        print()
        return True


if __name__ == '__main__':
    arr = [1, 2, 6, 3, 9, 4, 7, 8]
    list = DoublyLinkedList()
    for i in arr:
        list.insert(i)

    list.printLinkedList()
    list.delete(1)
    list.printLinkedList()
    list.delete(4)
    list.printLinkedList()
    list.delete(6)
    list.printLinkedList()
    list.delete(80)
    list.printLinkedList()
