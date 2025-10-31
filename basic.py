class Node:
    def __init__ (self, data, next = None):
        self.data = data
        self.next = next
    class Linkedlist:
        def __init__(self):
            self.head = None
            self.tail = None
        def addStart (self,x):
            newNode = Node(data = x)
            if self.head is None:
                self.head = newNode
                self.tail = newNode
            else:
                newNode.next = self.head
                self.head = newNode
        def addEnd(self, x):
            newNode = Node(data = x)
            if self.head is None:
                self.head = newNode
                self.tail = newNode
            else:
                self.tail.next = newNode
                newNode.next = None
                self.tail = newNode
                
        def show(self):
            curr = self.head
            while curr:
                print(curr.data)
                curr = curr.next
        def deleteX(self,x ):
            if self.head is None:
                return
            curr = self.head
            prev = None
            while curr.data !=x
                prev = curr
                curr = curr.next
            prev.next= curr.next
            curr.next= None
            if curr == self.tail:
                self.tail = prev
    
llist = Linkedlist()
Data= [2,4,5,6,7]
for i in range(len(Data)):
    llist.addStrart(Data([i]))
    llist.addEnd(Data[i])
llist.deletex(3)
llist.show()