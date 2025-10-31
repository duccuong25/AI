


class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def insertLast(self, x): # O(1) | array: O(1)
        newNode = Node(x)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:    
            self.tail.next = newNode
            self.tail = newNode
    
    def insertFirst(self, x): # O(1) | array: O(n)
        newNode = Node(x)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def removeFirst(self): # O(1)
        if self.isEmpty():
            print("list is empty")
            return
        if self.head == self.tail: # there is 1 node
            self.head = self.tail = None
        else: # there are more than 1 node
            self.head = self.head.next

    def removeLast(self): # O(n)
        if self.isEmpty():
            print("list is empty")
            return
        if self.head == self.tail: # there is 1 node
            self.head = self.tail = None
        else: # there are more than 1 node
            current = self.head
            while current.next is not self.tail:
                current = current.next
            current.next = None
            self.tail = current
    
    def removeData(self, x): # O(n)
        if self.isEmpty():
            print("list is empty")
            return
        if self.head.data == x:
            self.removeFirst()
            return
        current = self.head
        while current.next is not None:
            if current.next.data == x:
                if current.next is self.tail:
                    self.tail = current
                current.next = current.next.next
                break
            else:
                current = current.next
        
        

    def disp(self): 
        if self.isEmpty():
            print("list is empty")
        else:
            current = self.head # start at head
            while current is not None:
                print(current.data, end = "  ") # print out data of current node
                current = current.next # move to the next node
            print()

    def dispRec(self):
        if(self.isEmpty()):
            print("list is empty")
        else:
            print("recursion: tail --> head")
            self.dispRec_(self.head)

    def dispRec_(self, node):
        if node is None: return
        self.dispRec_(node.next)
        print(node.data, end = "  ")
        

# sList = SinglyLinkedList()
# sList.insertLast(7)
# sList.insertLast(6)
# sList.insertLast(1)
# sList.disp()     
# sList.insertFirst(4)
# sList.insertFirst(5)
# sList.insertFirst(9)
# sList.insertFirst(3)
# sList.disp()
# sList.removeFirst()
# sList.disp()
# sList.removeLast()
# sList.disp()
# sList.removeData(6)
# sList.disp()
# sList.insertLast(10)
# sList.disp()
# sList.dispRec()
