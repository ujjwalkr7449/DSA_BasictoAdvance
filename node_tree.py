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