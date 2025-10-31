'''
First in first out
'''

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class ListQueue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def isEmpty(self):
        return self.head == None

    def enqueue(self, x):
        newNode = Node(x)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:    
            self.tail.next = newNode
            self.tail = newNode

    def dequeue(self)->Node:
        if self.isEmpty():
            # print("list is empty")
            return None
        temp = self.head
        if self.head == self.tail: # there is 1 node
            self.head = self.tail = None
        else: # there are more than 1 node
            self.head = self.head.next
        return temp
    
    def front(self)->Node:
        if self.isEmpty():
            print("list is empty")
            return None
        return self.head

    def disp(self): 
        if self.isEmpty():
            print("list is empty")
        else:
            print("front --> rear")
            current = self.head # start at head
            while current is not None:
                print(current.data, end = "  ") # print out data of current node
                current = current.next # move to the next node
            print()


lQueue = ListQueue()
lQueue.enqueue(5)
lQueue.enqueue(2)
lQueue.enqueue(4)
lQueue.enqueue(3)
lQueue.disp()
node = lQueue.dequeue()
if node:
    print(f"dequeue: {node.data}")
lQueue.disp()