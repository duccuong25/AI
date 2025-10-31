'''
is BST where each node is balanced
balanced node: |height(leftsubtree) - height(rightsubtree)| < 2
imbalanced node: |height(leftsubtree) - height(rightsubtree)| > 1
'''

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root == None
    
    def leftRotate(self, node)->Node:
        a = node.right
        b = a.left
        a.left = node
        node.right = b
        return a

    def rightRotate(self, node)->Node:
        a = node.left
        b = a.right
        a.right = node
        node.left = b
        return a

    def height(self, node):
        if node is None: return 0
        return max(self.height(node.left), self.height(node.right)) + 1
    def balanceFactor(self, node):
        return self.height(node.left) - self.height(node.right)

    def insert(self, x):
        def insert_(x, node)->Node:
            if node is None: return Node(x)
            elif x < node.data: node.left = insert_(x, node.left)
            elif x > node.data: node.right = insert_(x, node.right)
            return self.balance(node)
        self.root = insert_(x, self.root)

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
            return self.balance(node)
        self.root = deleteByCopying_(x, self.root)
    
    def balance(self, node)->Node:
        # check balanced!
        if self.balanceFactor(node) < -1: # h(right) > h(left)
            if self.balanceFactor(node.right) > 0:
                node.right = self.rightRotate(node.right)
            node = self.leftRotate(node)
        elif self.balanceFactor(node) > 1:  # h(right) < h(left)
            if self.balanceFactor(node.left) < 0:
                node.left = self.leftRotate(node.left)
            node = self.rightRotate(node)
        return node

    def preOrder(self):
        def preOrder_(node):
            if node is None: return
            print(node.data, end ="  ") # visit node
            preOrder_(node.left) # visit left child
            preOrder_(node.right) # visit left child
        if self.isEmpty(): print("tree is empty")
        else: 
            print("pre-order traversal") 
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
            print("post-order traversal") 
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
            print("in-order traversal") 
            inOrder_(self.root)
            print()

avl = AVLTree()
avl.insert(100)
avl.insert(50)
avl.insert(150)
avl.insert(120)
avl.insert(180)
avl.insert(30)
avl.insert(70)
avl.insert(20)
avl.preOrder()
avl.inOrder()
avl.postOrder()
# avl.insert(200)
# avl.preOrder()
# avl.inOrder()
# avl.postOrder()
avl.deleteByCopying(100)
avl.preOrder()
avl.inOrder()
avl.postOrder()