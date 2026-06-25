class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def height(node):
    if not node:
        return 0
    return node.height

def balance(node):
    if not node:
        return 0
    return height(node.left) - height(node.right)

def right_rotate(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))

    return x

def left_rotate(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))

    return y

def insert(node, key):
    if not node:
        return Node(key)

    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    node.height = 1 + max(height(node.left), height(node.right))

    bf = balance(node)

    # LL Case
    if bf > 1 and key < node.left.key:
        return right_rotate(node)

    # RR Case
    if bf < -1 and key > node.right.key:
        return left_rotate(node)

    # LR Case
    if bf > 1 and key > node.left.key:
        node.left = left_rotate(node.left)
        return right_rotate(node)

    # RL Case
    if bf < -1 and key < node.right.key:
        node.right = right_rotate(node.right)
        return left_rotate(node)

    return node

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

# Driver Code
root = None
values = [10, 20, 30, 40, 50, 25]

for value in values:
    root = insert(root, value)

print("AVL Tree Inorder Traversal:")
inorder(root)