class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class ListStack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def push(self, x):
        newNode = Node(x)
        if self.isEmpty():
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def pop(self):
        if self.isEmpty():
            print("list is empty")
            return None
        temp = self.head
        self.head = self.head.next
        return temp

    def peak(self):
        pass

    def disp(self):
        if self.isEmpty():
            print("list is empty")
        else:
            print("top --> bottom")
            current = self.head # start at head
            while current is not None:
                print(current.data, end = "  ") # print out data of current node
                current = current.next # move to the next node
            print()

lStack = ListStack()
lStack.push(5)
# lStack.push(2)
# lStack.push(4)
# lStack.push(3)
lStack.disp()
print(f"pop: {lStack.pop().data}")
lStack.disp()