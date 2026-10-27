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