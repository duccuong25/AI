'''
Tree:
- Non-linear, herachical structure: parent-children
- 1 root, many leaves
- leaf: external node
- nodes, not leaves: internal nodes
- each node has any number of children
- node1 --> node2 --> node3, node2 --> node4
+ node1 is node2's parent
+ node2 is node1's child
+ node1 is node3's ancestor
+ node3 is node1's decendant
+ node3 and node4 are siblings
- height of the tree: from root to  leaf 
- level of root = 0

Binary tree:
- is tree where each node has at most 2 children

Binary Search Tree:
- is binary tree where key(left child) < key(parent) < key(right child)
- data of node is key
'''

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

# data of node is considered as its key
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root == None

    def insert(self, x):
        newNode = Node(x)
        if self.isEmpty():
            self.root = newNode
            return
        current = self.root
        while True:
            if x > current.data:
                if current.right is None:
                    current.right = newNode
                    return
                current = current.right
            if x < current.data:
                if current.left is None:
                    current.left = newNode
                    return
                current = current.left
            if x == current.data:
                print("exist!")
                return

    def insertRec(self, x):
        def insertRec_(node)->Node:
            if node is None:
                return Node(x)
            if x > node.data:
                node.right = insertRec_(node.right)
            if x < node.data:
                node.left = insertRec_(node.left)
            return node
        self.root = insertRec_(self.root)

    def findMostRight(self, node)->Node:
        while node.right is not None:
            node = node.right
        return node

    def deleteByCopying(self, x):
        def deleteByCopying_(x, node)->Node:
            if(node is None): return Node
            if x > node.data: node.right = deleteByCopying_(x, node.right)
            elif x < node.data: node.left = deleteByCopying_(x, node.left)
            else: 
                # found!
                if node.left is None: # 1 right child
                    node = node.right
                    return node
                if node.right is None: # 1 left child
                    node = node.left
                    return node
                # 2 children
                mostRightNode = self.findMostRight(node.left)
                node.data = mostRightNode.data
                node.left = deleteByCopying_(mostRightNode.data, node.left)
            return node
        self.root = deleteByCopying_(x, self.root)

    def deleteByMerging(self, x):
        def deleteByMerging_(x, node):
            if node is None: return node
            if x < node.data: node.left = deleteByMerging_(x, node.left)
            elif x > node.data: node.right = deleteByMerging_(x, node.right)
            else:
                if node.left is None:
                    node = node.right
                    return node
                if node.right is None:
                    node = node.left
                    return node
                mostRightNode = self.findMostRight(node.left)
                mostRightNode.right = node.right
                node = node.left
            return node
        self.root = deleteByMerging_(x, self.root)

    def search(self, x):
        def search_(x, node):
            if node is None or node.data == x: return node
            if x > node.data: return search(x, node.right)
            if x < node.data: return search(x, node.left)
        return search_(x, self.root)



    def height(self, node):
        if node is None: return 0
        return max(self.height(node.left), self.height(node.right)) + 1
        
    def treeHeight(self):
        return self.height(self.root)

    def preOrder(self):
        def preOrder_(node):
            if node is None: return
            print(node.data, end ="  ") # visit node
            preOrder_(node.left) # visit left child
            preOrder_(node.right) # visit left child
        if self.isEmpty(): print("tree is empty")
        else: 
            preOrder_(self.root)
            print()

    def postOrder(self):
        def postOrder_(node):
            if node is None: return
            postOrder_(node.left) # visit left child
            postOrder_(node.right) # visit left child
            print(node.data, end ="  ") # visit node
        if self.isEmpty(): print("tree is empty")
        else: 
            postOrder_(self.root)
            print()
    
    def inOrder(self):
        def inOrder_(node):
            if node is None: return
            inOrder_(node.left) # visit left child
            print(node.data, end ="  ") # visit node
            inOrder_(node.right) # visit left child
        if self.isEmpty(): print("tree is empty")
        else: 
            inOrder_(self.root)
            print()

bst = BinarySearchTree()
# bst.insert(100)
# bst.insert(50)
# bst.insert(150)
# bst.insert(30)
# bst.insert(70)
# bst.insert(60)
# bst.insert(80)
# bst.insert(120)
# bst.insert(140)
bst.insertRec(100)
bst.insertRec(50)
bst.insertRec(150)
bst.insertRec(30)
bst.insertRec(70)
bst.insertRec(60)
bst.insertRec(80)
bst.insertRec(120)
bst.insertRec(140)
bst.preOrder()
bst.postOrder()
bst.inOrder()
print(f"height of the tree: {bst.treeHeight()}")
# bst.deleteByCopying(100)
bst.deleteByMerging(50)
bst.preOrder()
bst.postOrder()
bst.inOrder()
