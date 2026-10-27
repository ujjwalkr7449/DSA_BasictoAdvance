#Python's collections.deque is a good choice for implementing a queue.
from collections import deque

queue = deque()

# Enqueue
queue.append(10)
queue.append(20)
queue.append(30)

print(queue)

# Dequeue
queue.popleft()

print(queue)

# Front element
print(queue[0])

#Question 1: Implement a queue using a list
queue = []

queue.append(10)
queue.append(20)
queue.append(30)

print(queue)

#Question 2: Remove the first element
queue = [10, 20, 30, 40]

queue.pop(0)

print(queue)

#Question 3: Find the front element
queue = [10, 20, 30, 40]

print(queue[0])

#Check whether the queue is empty
queue = []

if len(queue) == 0:
    print("Queue is empty")
else:
    print("Queue is not empty")
    
    
#Question 5: Find the size of a queue
queue = [10, 20, 30, 40, 50]

print(len(queue))

#Question 6: Reverse a queue
from collections import deque

queue = deque([10, 20, 30, 40])

queue.reverse()

print(queue)