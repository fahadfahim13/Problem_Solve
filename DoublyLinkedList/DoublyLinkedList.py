from Binary_Tree_Python.Node import LinkedNode


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.total_nodes = 0

    def insert(self, data):
        if data is None:
            return False

        node = LinkedNode(data)
        if self.total_nodes == 0:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = self.tail.next
        self.total_nodes = self.total_nodes + 1
        return True

    def printLinkedList(self):
        if self.total_nodes == 0:
            print('No Nodes')
            return False
        node = self.head
        for i in range(0, self.total_nodes):
            print(node.value, end=" ")
            node = node.next
        print()
        return True