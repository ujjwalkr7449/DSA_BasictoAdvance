stack = []

# Push elements
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack:", stack)

# Pop element
stack.pop()

print("After pop:", stack)


stack = [10, 20, 30]

top = stack[-1]

print("Top element:", top)

stack = []

if len(stack) == 0:
    print("Stack is empty")
else:
    print("Stack is not empty")

stack = []

while True:

    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:

        value = int(input("Enter value: "))
        stack.append(value)

        print("Element pushed")

    elif choice == 2:

        if len(stack) == 0:
            print("Stack is empty")
        else:
            print("Removed:", stack.pop())

    elif choice == 3:

        if len(stack) == 0:
            print("Stack is empty")
        else:
            print("Top:", stack[-1])

    elif choice == 4:

        print("Stack:", stack)

    elif choice == 5:

        break

    else:
        print("Invalid choice")
        
text = "python"

stack = []

for char in text:
    stack.append(char)

result = ""

while stack:
    result += stack.pop()

print(result)



s = "({[]})"

stack = []

pairs = {
    ")": "(",
    "}": "{",
    "]": "["
}

for char in s:

    if char in "({[":
        stack.append(char)

    elif char in ")}]":

        if not stack or stack[-1] != pairs[char]:
            print("Not Balanced")
            break

        stack.pop()

else:

    if not stack:
        print("Balanced")
    else:
        print("Not Balanced")
        
        
#QUeue
from collections import deque

queue = deque()

# Enqueue
queue.append(10)
queue.append(20)
queue.append(30)

print("Queue:", queue)

# Dequeue
queue.popleft()

print("After dequeue:", queue)


from collections import deque

queue = deque([10, 20, 30])

print("Front:", queue[0])

from collections import deque

queue = deque()

if not queue:
    print("Queue is empty")
else:
    print("Queue is not empty")