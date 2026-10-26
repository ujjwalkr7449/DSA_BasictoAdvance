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