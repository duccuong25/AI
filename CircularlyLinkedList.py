'''
sequence of nodes in which tail.next is head
'''

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class CircularlyLinkedList:
    def __init__(self):
        self.tail = None

    def isEmpty(self):
        return self.tail == None
    
    def insertFirst(self, x):
        newNode = Node(x)
        if self.isEmpty():
            self.tail = newNode
            self.tail.next = self.tail
        else:
            newNode.next = self.tail.next
            self.tail.next = newNode

    def insertLast(self, x):
        self.insertFirst(x)
        self.tail = self.tail.next

    def removeFirst(self):
        if self.isEmpty():
            print("list is empty")
            return
        if self.tail.next == self.tail:
            self.tail = None
        else:
            self.tail.next = self.tail.next.next


    def removeLast(self):
        if self.isEmpty():
            print("list is empty")
            return
        if self.tail.next == self.tail: # 1 node
            self.tail = None
        else: # more than 1 node
            current = self.tail.next
            while current.next is not self.tail:
                current = current.next
            current.next = self.tail.next
            self.tail = current


    def disp(self):
        if self.isEmpty():
            print("list is empty")
            return
        current = self.tail.next # head
        while current is not self.tail:
            print(current.data, end = "  ")
            current = current.next
        print(current.data)

cList = CircularlyLinkedList() 
cList.insertFirst(5)
cList.insertFirst(2)
cList.insertFirst(4)
cList.insertFirst(3)
cList.disp()
# cList.removeLast()
cList.removeFirst()
cList.disp()
