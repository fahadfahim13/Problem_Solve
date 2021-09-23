from LinkedList_Python.Link import Link


class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def insert(self, data):
        if data is None:
            return False

        newlink = Link()
        newlink.data = data
        newlink.next = None
        if self.length == 0:
            self.head = newlink
            self.tail = self.head
        else:
            self.tail.next = newlink
            self.tail = self.tail.next

        self.length = self.length + 1
        return True

    def deleteLast(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.length = 0
            self.head = None
            self.tail = None
            return None

        temp = self.head
        while temp.next is not None and temp.next.data != self.tail.data:
            temp = temp.next

        if temp.next.data == self.tail.data:
            newtemp = self.tail.data
            temp.next = None
            self.tail = temp
            self.length = self.length - 1
            return newtemp

        return None

    def getLast(self):
        if self.length == 0:
            return None
        return self.tail.data

    def getLength(self):
        return self.length

    def deleteFirst(self):
        if self.length == 0:
            return None
        tmp = self.head
        self.head = self.head.next
        self.length = self.length - 1
        return tmp.data

    def printList(self):
        if self.length == 0:
            print('')
            return
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next

        return

