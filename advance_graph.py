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

"""B. Bellman-Ford Algorithm (Handles negative weights, detects cycles)"""
def bellman_ford(vertices, edges, start):
  # edges format: [(u, v, weight), ...]
  dist = {v: float("inf") for v in vertices}
  dist[start] = 0

  for _ in range(len(vertices) - 1):
    for u, v, w in edges:
      if dist[u] != float("inf") and dist[u] + w < dist[v]:
        dist[v] = dist[u] + w

  # Check for negative weight cycles
  for u, v, w in edges:
    if dist[u] != float("inf") and dist[u] + w < dist[v]:
      raise ValueError("Graph contains a negative weight cycle")
  return dist

#C. Floyd-Warshall Algorithm (All-Pairs Shortest Path)
def floyd_warshall(n, edges):
  # n: number of nodes (0 to n-1)
  dist = [[float("inf")] * n for _ in range(n)]
  for i in range(n):
    dist[i][i] = 0
  for u, v, w in edges:
    dist[u][v] = w

  for k in range(n):
    for i in range(n):
      for j in range(n):
        if dist[i][k] + dist[k][j] < dist[i][j]:
          dist[i][j] = dist[i][k] + dist[k][j]
  return dist

"""3. Minimum Spanning Tree (MST)
A. Kruskal's Algorithm (Edge-based using DSU)
Python"""
def kruskal(n, edges):
  # edges format: [(weight, u, v), ...]
  edges.sort()
  dsu = DSU(n)
  mst = []
  mst_weight = 0

  for w, u, v in edges:
    if dsu.union(u, v):
      mst.append((u, v, w))
      mst_weight += w
  return mst, mst_weight

"""B. Prim's Algorithm (Vertex-based using Priority Queue)"""
def prim(n, graph):
  # graph format: {u: [(v, weight), ...]}
  visited = [False] * n
  min_heap = [(0, 0, -1)]  # (weight, current_node, parent)
  mst_weight = 0
  mst = []

  while min_heap:
    w, u, p = heapq.heappop(min_heap)
    if visited[u]:
      continue
    visited[u] = True
    if p != -1:
      mst.append((p, u, w))
      mst_weight += w

    for v, weight in graph[u]:
      if not visited[v]:
        heapq.heappush(min_heap, (weight, v, u))
  return mst, mst_weight

"""4. Advanced Graph Traversals & Properties
A. Topological Sorting (Kahn's Algorithm using In-Degrees)"""
from collections import deque


def kahn_topological_sort(n, graph):
  # graph format: {u: [v, ...]}
  in_degree = [0] * n
  for u in graph:
    for v in graph[u]:
      in_degree[v] += 1

  queue = deque([i for i in range(n) if in_degree[i] == 0])
  topo_order = []

  while queue:
    u = queue.popleft()
    topo_order.append(u)
    for v in graph.get(u, []):
      in_degree[v] -= 1
      if in_degree[v] == 0:
        queue.append(v)

  if len(topo_order) != n:
    raise ValueError("Graph has a cycle; topological sort not possible.")
  return topo_order