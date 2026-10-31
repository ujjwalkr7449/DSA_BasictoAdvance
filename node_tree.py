class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

n1 = Node(10)
n2 = Node(20)

n1.next = n2

print(n1.data)       # 10
print(n1.next.data)  # 20


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
#Step 2: Create tree
root = Node(10)

root.left = Node(20)
root.right = Node(30)

root.left.left = Node(40)
root.left.right = Node(50)

root.right.left = Node(60)

#Step 3: Print tree values
print(root.data)
print(root.left.data)
print(root.right.data)
print(root.left.left.data)
#Tree Traversal

def preorder(root):
    if root is None:
        return

    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)
    
#B. Inorder Traversal
#Order: Left → Root → Right
def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)
    
#C. Postorder Traversal
#Order: Left → Right → Root
def postorder(root):
    if root is None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")
#D. Level Order Traversal (BFS)
#Visits nodes level by level using a queue.
from collections import deque

def level_order(root):
    if root is None:
        return

    q = deque([root])

    while q:
        node = q.popleft()
        print(node.data, end=" ")

        if node.left:
            q.append(node.left)

        if node.right:
            q.append(node.right)

#Insert operation in BST
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):

    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)

    elif data > root.data:
        root.right = insert(root.right, data)

    return root


root = None

values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    root = insert(root, value)

#Search operation in BST
def search(root, key):

    if root is None:
        return False

    if root.data == key:
        return True

    if key < root.data:
        return search(root.left, key)

    return search(root.right, key)


print(search(root, 60))
print(search(root, 100))