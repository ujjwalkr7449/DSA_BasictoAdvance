"""1. What is a Graph?
A graph is a non-linear data structure made up of:
- Vertex (Node): A point in the graph.
- Edge: A connection between two nodes."""

"""
types of Graphs:
1. Undirected Graph:
Edges have no direction. If A connects to B, you can travel from A to B and B to A.
2. Directed Graph:
Edges have directions. If A → B, you cannot automatically travel from B → A.
3. Weighted Graph:
Every edge can have a cost, distance, or weight.
"""
""" Graph Representation in Python:
1. Adjacency Matrix:An adjacency list stores each node along with its neighboring nodes.
Remember: graph['A'] returns the neighbors of node A.
"""
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

print(graph)
print(graph['A'])

"""Method 2: Adjacency Matrix:
An adjacency matrix uses a 2D list. 1 means an edge exists, and 0 means no edge exists."""
