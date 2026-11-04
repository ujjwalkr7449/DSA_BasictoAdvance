"""1. Disjoint Set Union (DSU / Union-Find)
Essential helper structure used in Kruskal's algorithm and cycle detection."""

class DSU:

  def __init__(self, n):
    self.parent = list(range(n))
    self.rank = [0] * n

  def find(self, i):
    if self.parent[i] == i:
      return i
    self.parent[i] = self.find(self.parent[i])  # Path compression
    return self.parent[i]

  def union(self, i, j):
    root_i = self.find(i)
    root_j = self.find(j)
    if root_i != root_j:
      if self.rank[root_i] < self.rank[root_j]:
        self.parent[root_i] = root_j
      elif self.rank[root_i] > self.rank[root_j]:
        self.parent[root_j] = root_i
      else:
        self.parent[root_j] = root_i
        self.rank[root_i] += 1
      return True
    return False

"""2. Shortest Path Algorithms
A. Dijkstra's Algorithm (Single-Source Shortest Path with non-negative weights)"""
import heapq


def dijkstra(graph, start):
  # graph format: {u: [(v, weight), ...]}
  distances = {node: float("inf") for node in graph}
  distances[start] = 0
  pq = [(0, start)]

  while pq:
    current_dist, u = heapq.heappop(pq)
    if current_dist > distances[u]:
      continue
    for v, weight in graph[u]:
      distance = current_dist + weight
      if distance < distances[v]:
        distances[v] = distance
        heapq.heappush(pq, (distance, v))
  return distances