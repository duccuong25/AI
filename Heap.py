'''
- HEAP: is (nearly) complete binary tree
where key(parent) <= key(children) : min heap
- complete binary tree;
+ each node has 2 children or no child
+ all leaves have the same level
- array or linked list to implement
- applications: find max min, sort, priority queue*
'''

class Node:
    def __init__(self, x):
        self.data = x

class MinHeap:
    def __init__(self, cap = 7):
        self.capacity = cap
        self.length = 0
        self.arrayNodes = [""]*cap
    
    def isEmpty(self):
        return self.length == 0

    def isFull(self):
        return self.length == self.capacity

    def increaseCap(self):
        newCap = self.capacity * 2
        newArray = [""] * newCap
        for i in range(self.length):
            newArray[i] = self.arrayNodes[i]
        self.arrayNodes = newArray
        self.capacity = newCap

    def insert(self, x):
        if(self.isFull()): self.increaseCap()
        self.arrayNodes[self.length] = Node(x)
        self.length += 1
        self.heapifyUp(self.length-1)

    def heapifyUp(self, idx):
        pIdx = (idx - 1)//2
        if pIdx < 0: return
        if(self.arrayNodes[idx].data < self.arrayNodes[pIdx].data):
            temp = self.arrayNodes[idx]
            self.arrayNodes[idx] = self.arrayNodes[pIdx]
            self.arrayNodes[pIdx] = temp
            self.heapifyUp(pIdx)



    def search(self, x): # breadth first search
        for i in range(self.length):
            if self.arrayNodes[i].data == x:
                return i
        return -1 

    def delete(self, x):
        idx = self.search(x)
        if(idx != -1):
            # copy the last to the node deleted
            self.arrayNodes[idx] = self.arrayNodes[self.length-1]
            self.length -= 1
            self.heapifyDown(idx)
            self.heapifyUp(idx)

    def heapifyDown(self, idx):
        '''
        key(p) > key(l) or key(p) > key(r)
        '''
        pIdx = idx # pIdx is the next index that idx moves to
        lIdx = pIdx*2+1
        rIdx = pIdx*2+2
        # if pIdx > self.length // 2 - 1: return
        if rIdx < self.length and self.arrayNodes[pIdx].data >= self.arrayNodes[rIdx].data:
            pIdx = rIdx
        if lIdx < self.length and self.arrayNodes[pIdx].data >= self.arrayNodes[lIdx].data:
            pIdx = lIdx
        if pIdx != idx:
            self.arrayNodes[pIdx], self.arrayNodes[idx] = self.arrayNodes[idx], self.arrayNodes[pIdx]
            self.heapifyDown(pIdx)

        

    def preOrder(self):
        '''
        visit node
        visit left child
        visit right child
        '''
        def preOrder_(idx):
            if idx >= self.length: return
            print(self.arrayNodes[idx].data, end = "  ")
            lIdx = idx * 2 + 1
            preOrder_(lIdx)
            rIdx = idx * 2 + 2
            preOrder_(rIdx)
        preOrder_(0)
        print()
        
    def inOrder(self):
        def inOrder_(idx):
            if idx >= self.length: return
            lIdx = idx * 2 + 1
            inOrder_(lIdx)
            print(self.arrayNodes[idx].data, end = "  ")
            rIdx = idx * 2 + 2
            inOrder_(rIdx)
        inOrder_(0)
        print()

    def disp(self):
        if(not self.isEmpty()):
            print("preOrder")
            self.preOrder()
            print("inOrder")
            self.inOrder()

# mH = MinHeap()
# mH.insert(3)
# mH.insert(15)
# mH.insert(9)
# mH.insert(17)
# mH.insert(20)
# mH.insert(11)
# mH.insert(14)
# mH.insert(22)
# mH.insert(23)
# mH.insert(25)
# mH.insert(27)
# mH.insert(18)
# mH.insert(12)
# mH.disp()
# # mH.insert(2)
# # mH.disp()
# mH.delete(20)
# mH.disp()