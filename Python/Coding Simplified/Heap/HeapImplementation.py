class Heap:
    size: int
    arr: list[int]

    def __init__(self):
        self.size = 0
        self.arr = []

    def insertValue(self, val: int) -> None:
        self.arr.append(val)
        index = self.size
        parent = (index - 1) // 2
        while parent >= 0 and self.arr[parent] < self.arr[index]:
            self.arr[parent], self.arr[index] = self.arr[index], self.arr[parent]
            index = parent
            parent = (index - 1) // 2
        self.size += 1

    def printHeap(self):
        for i in self.arr:
            print(i, end=" ")
        print()

    def getMax(self):
        return self.arr[0]

    def maxHeapify(self, idx):
        if idx >= self.size:
            return
        first = 2 * idx + 1
        second = 2 * idx + 2
        num = self.arr[idx]
        final = first
        if first < self.size and num < self.arr[first]:
            self.arr[idx], self.arr[first] = self.arr[first], self.arr[idx]
            final = first
        elif second < self.size and num < self.arr[second]:
            self.arr[idx], self.arr[second] = self.arr[second], self.arr[idx]
            final = second
        self.maxHeapify(final)

    def removeMax(self):
        max_num = self.arr[0]
        self.arr[0] = self.arr[-1]
        self.arr.pop()
        self.size -= 1
        self.maxHeapify(0)
        return max_num
    
    def buildHeap(self, arr_num: list[int]):
        self.arr = arr_num
        self.size = len(arr_num)
        idx = self.size // 2 - 1
        for i in range(idx, -1, -1):
            self.maxHeapify(i)
        self.printHeap()


def main():
    arr = [10, 7, 11, 30, 20, 38, 2, 45]
    heap1 = Heap()
    heap1.buildHeap(arr)
    heap = Heap()
    for i in arr:
        heap.insertValue(i)
        heap.printHeap()
    print(f"Max of Heap: {heap.removeMax()}")
    heap.printHeap()
    print(f"Max of Heap: {heap.removeMax()}")
    heap.printHeap()
    print(f"Max of Heap: {heap.removeMax()}")
    heap.printHeap()
    print(f"Max of Heap: {heap.removeMax()}")
    heap.printHeap()
    print(f"Max of Heap: {heap.removeMax()}")
    heap.printHeap()
    print(f"Max of Heap: {heap.removeMax()}")
    heap.printHeap()


if __name__ == '__main__':
    main()
