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