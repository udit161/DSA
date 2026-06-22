class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

    def preOrder(self):
        if self is not None:
            print(self.data, end=' ')
            if self.left is not None:
                self.left.preOrder()
            if self.right is not None:
                self.right.preOrder()

root = Node(1)
root.left = Node(3)
root.right = Node(5)     

root.left.left = Node(2)
root.left.right = Node(4)

root.right.right = Node(8)

print("Preorder Traversal: ")
root.preOrder()