'''

'''

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def isEmpty(self):
        return self.head == None

    def enqueue(self, x):
        newNode = Node(x)
        if self.isEmpty():
            self.head = self.tail = newNode
            return
        if self.head.data >= x:
            newNode.next = self.head
            self.head = newNode
            return
        if self.tail.data <= x:
            self.tail.next = newNode
            self.tail = newNode
            return
        # head.data > x > tail.data
        current = self.head
        while current.next.data < x:
            current = current.next
        # x >= current.next.data --> current.data > x
        newNode.next = current.next
        current.next = newNode

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

# pQueue = PriorityQueue()
# pQueue.enqueue(5)
# pQueue.enqueue(9)
# pQueue.enqueue(4)
# pQueue.enqueue(7)
# pQueue.disp()