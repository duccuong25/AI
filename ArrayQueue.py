class Node:
    def __init__(self, x):
        self.data = x

class ArrayQueue:
    def __init__(self, cap = 5):
        self.capacity = cap
        self.fIdx = -1
        self.length = 0
        self.arrayNodes = [""] * cap

    def isEmpty(self):
        return self.length == 0

    def isFull(self):
        return self.length == self.capacity

    def enqueue(self, x):
        newNode = Node(x)
        if self.isEmpty():
            self.fIdx = 0
            self.arrayNodes[self.fIdx] = newNode
            self.length += 1
            return
        if self.isFull():
            self.increaseCap()
        lIdx = (self.fIdx + self.length) % self.capacity
        self.arrayNodes[lIdx] = newNode
        self.length += 1
    
    def dequeue(self)->Node:
        if self.isEmpty(): return None
        temp = self.arrayNodes[self.fIdx]
        self.fIdx = ( self.fIdx + 1 ) % self.capacity
        self.length -= 1
        # if(self.length==0): self.fIdx = -1
        return temp

    def front(self):
        if self.isEmpty():
            return None
        return self.arrayNodes[self.fIdx]

    def increaseCap(self):
        newCap = self.capacity * 2
        newArray = [""] * newCap
        for i in range(self.length):
            idx_to_copy = (self.fIdx + i) % self.capacity
            newArray[i] = self.arrayNodes[idx_to_copy]
        self.capacity = newCap
        self.arrayNodes = newArray
        self.fIdx = 0

    def disp(self):
        if self.isEmpty():
            print("array is empty")
            return
        for i in range(self.length):
            idx = (self.fIdx + i) % self.capacity
            print(self.arrayNodes[idx].data, end = "  ")
        print(f"\nfIdx = {self.fIdx}, length = {self.length}, capacity = {self.capacity}")

# aQueue = ArrayQueue()
# aQueue.enqueue(5)
# aQueue.enqueue(4)
# aQueue.enqueue(3)
# aQueue.enqueue(2)
# aQueue.disp()
# node = aQueue.dequeue()
# if node:
#     print("dequeue: ", node.data)
# aQueue.disp()
# node = aQueue.dequeue()
# if node:
#     print("dequeue: ", node.data)
# aQueue.disp()
# aQueue.enqueue(9)
# aQueue.enqueue(10)
# aQueue.disp()
