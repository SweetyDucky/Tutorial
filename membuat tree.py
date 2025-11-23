class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Membangun tree
root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')

# Traversal
def preorder(node):
    if node:
        print(node.data, end=' ')
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=' ')
        inorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=' ')

# Output traversal
print("Preorder: ", end='')
preorder(root)
print("\nInorder: ", end='')
inorder(root)
print("\nPostorder: ", end='')
postorder(root)

#misalkan ini adalah kode revisi
