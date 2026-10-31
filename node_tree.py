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