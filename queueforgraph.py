"""
1. What is a Queue?
A Queue follows FIFO — First In, First Out.

The element inserted first is removed first, just like people standing in a line.
"""

"""2. Queue operations in Python
Use deque from Python's collections module."""

from collections import deque

q = deque()

q.append(10)  # Add element
q.append(20)
q.append(30)

print(q)

print(q.popleft())  # Remove first element
print(q)
"""Remember these two operations:
- append() → adds an element to the rear.
- popleft() → removes an element from the front."""

from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}

def bfs(start):
    visited = set([start])
    q = deque([start])

    while q:
        node = q.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)

bfs('A')



from collections import deque

q = deque()

q.append(5)
q.append(10)
q.append(15)

q.popleft()
q.append(20)

print(list(q))


"""Queue in Python: Functions, Methods & Keywords (DSA)
In Python DSA, a Queue follows FIFO (First In, First Out). 
For interviews, you should understand the methods, 
built-in functions, and keywords used when implementing a queue."""

"""1. Queue methods using deque
First, import deque from the collections module."""

from collections import deque

q = deque()


"""2. Built-in functions used with a Queue
Function	Purpose	Example
len(q)	Count elements	len(q)
list(q)	Convert queue to list	list(q)
bool(q)	Check whether queue is non-empty	bool(q)
print(q)	Display queue	print(q)
max(q)	Find maximum element	max(q)
min(q)	Find minimum element	min(q)
sum(q)	Sum numeric elements	sum(q)
"""