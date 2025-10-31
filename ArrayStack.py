class Node:
    def __init__(self, x):
        self.data = x

class ArrayStack:
    def __init__(self, cap = 5):
        self.capacity = cap
        self.length = 0
        self.arrayNodes = [""] * cap

    def isFull(self):
        return self.capacity == self.length

    def isEmpty(self):
        return self.length == 0

    def push(self, x):
        if self.isFull():
            # print("full")
            self.increaseCap()
            # return
        self.arrayNodes[self.length] = Node(x)
        self.length += 1

    def pop(self):
        if self.isEmpty(): 
            print("array is empty")
            return None
        temp = self.arrayNodes[self.length - 1]
        self.length -= 1
        return temp

    def peak(self): # top
        if self.isEmpty(): 
            print("array is empty")
            return None
        return self.arrayNodes[self.length - 1]

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
        print("bottom --> top")
        for i in range(self.length):
            print(self.arrayNodes[i].data, end = "  ")
        print(f"\nlength = {self.length}, capacity = {self.capacity}")


# aStack = ArrayStack()
# aStack.push(5)
# aStack.push(2)
# aStack.push(4)
# aStack.push(3)
# aStack.disp()
# print(f"pop: {aStack.pop().data}")
# aStack.disp()
# print(f"peak: {aStack.peak().data}")
# aStack.disp()