class Node:
    def __init__(self, x):
        self.data = x

class ArrayStructure:
    def __init__(self, cap = 5):
        self.capacity = cap
        self.length = 0
        self.arrayNodes = [""] * cap

    def isFull(self):
        # if(self.capacity == self.length): return True
        # return False
        return self.capacity == self.length

    def isEmpty(self):
        return self.length == 0

    def insertLast(self, x):
        if self.isFull():
            # print("full")
            self.increaseCap()
            # return
        self.arrayNodes[self.length] = Node(x)
        self.length += 1
    
    def insertFirst(self, x):
        if self.isFull(): self.increaseCap()
        # shift to the right 1 element
        for i in range(self.length, 0 , -1):
            self.arrayNodes[i] = self.arrayNodes[i-1]
        self.arrayNodes[0] = Node(x)
        self.length += 1
    
    def removeLast(self):
        if self.isEmpty(): 
            print("array is empty")
            return
        self.arrayNodes[self.length - 1] = ""
        self.length -= 1

    def removeFirst(self):
        if self.isEmpty():
            print("array is empty")
            return
        # shift to the left 1 element
        for i in range(self.length-1):
            self.arrayNodes[i] = self.arrayNodes[i+1]
        self.arrayNodes[self.length-1] = ""
        self.length -= 1

    def removeAtIdx(self, idx):
    
    def increaseCap(self):
        added_array = [""] * self.capacity
        self.arrayNodes = self.arrayNodes + added_array
        self.capacity *= 2
        # newCap = self.capacity * 2
        # newArray = [""] * newCap
        # for i in range(self.length):
        #     newArray[i] = self.arrayNodes[i]
        # self.arrayNodes = newArray
        # self.capacity = newCap

    def disp(self):
        for i in range(self.length):
            print(self.arrayNodes[i].data, end = "  ")
        print(f"\nlength = {self.length}, capacity = {self.capacity}")

aStruct = ArrayStructure(5)
aStruct.insertLast(5)
aStruct.insertLast(3)
aStruct.insertLast(2)
aStruct.disp()
aStruct.insertLast(4)
aStruct.insertLast(7)
aStruct.disp()
aStruct.insertLast(10)
aStruct.disp()
aStruct.removeFirst()
aStruct.disp()

    