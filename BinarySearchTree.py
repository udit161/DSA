class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
# for insertion
    @staticmethod
    def insert(root, value):
        if (root == None):
            return Node(value)
        if(root.data == value):
            return root
        if(root.data > value):
            root.left = Node.insert(root.left, value)
        else:         
           root.right = Node.insert(root.right, value)
        return root   


def InOrder(root):
    if(root != None):
        InOrder(root.left)
        print(root.data,end=' ')
        InOrder(root.right)       


def search(root, value):
    if(root == None):
        return False
        print("element not found")
    if(root.data == value):
        return True
        print("element found")
    if(root.data > value):
        return search(root.left, value)
    else:
        return search(root.right, value)    

root = None
root = Node.insert(root, 50)
root = Node.insert(root, 20)
root = Node.insert(root, 70)
root = Node.insert(root, 10)
root = Node.insert(root, 30)
root = Node.insert(root, 60)
root = Node.insert(root, 80)
InOrder(root)