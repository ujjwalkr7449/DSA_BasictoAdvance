class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

n1.next = n2
n2.next = n3

print(n1.data)
print(n1.next.data)
print(n1.next.next.data)

"""4. Implement a Complete Linked List"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


ll = LinkedList()

ll.head = Node(10)
ll.head.next = Node(20)
ll.head.next.next = Node(30)

ll.display()

"""Important Linked List Operations"""
#A. Insertion at Beginning
def insert_beginning(self, data):
    new_node = Node(data)

    new_node.next = self.head
    self.head = new_node
    
#B. Insertion at End
def insert_end(self, data):
    new_node = Node(data)

    if self.head is None:
        self.head = new_node
        return

    temp = self.head

    while temp.next:
        temp = temp.next

    temp.next = new_node
#C. Insertion at a Specific Position (0-based)
def insert_position(self, data, position):
    new_node = Node(data)

    if position < 0:
        return

    if position == 0:
        new_node.next = self.head
        self.head = new_node
        return

    temp = self.head

    for i in range(position - 1):
        if temp is None:
            return
        temp = temp.next

    if temp is None:
        return

    new_node.next = temp.next
    temp.next = new_node