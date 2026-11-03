"""1. Binary Search Trees (BST): Insertion and Validation
Question: Implement a function to insert a value into a Binary Search Tree and another function to validate if a given binary tree is a valid BST."""


class Node:

  def __init__(self, key):
    self.val = key
    self.left = None
    self.right = None
    
def insert_into_bst(root, key):
  if not root:
    return Node(key)
  if key < root.val:
    root.left = insert_into_bst(root.left, key)
  elif key > root.val:
    root.right = insert_into_bst(root.right, key)
  return root

def is_valid_bst(root, min_val=float("-inf"), max_val=float("inf")):
  if not root:
    return True
  if not (min_val < root.val < max_val):
    return False
  return is_valid_bst(root.left, min_val, root.val) and is_valid_bst(
      root.right, root.val, max_val
  )
# Example usage:
root = None
for val in [5, 3, 7, 2, 4]:
  root = insert_into_bst(root, val)

print("Is valid BST:", is_valid_bst(root))  # Output: True

"""2. Heaps / Priority Queues: Min-Heap Implementation
Question: Implement a Min-Heap from scratch supporting insertion (insert) and extracting the minimum element (extract_min).
"""
class MinHeap:

  def __init__(self):
    self.heap = []

  def _parent(self, i):
    return (i - 1) // 2

  def _left_child(self, i):
    return 2 * i + 1

  def _right_child(self, i):
    return 2 * i + 2

  def insert(self, val):
    self.heap.append(val)
    self._heapify_up(len(self.heap) - 1)

  def _heapify_up(self, i):
    p = self._parent(i)
    if i > 0 and self.heap[i] < self.heap[p]:
      self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
      self._heapify_up(p)

  def extract_min(self):
    if not self.heap:
      return None
    if len(self.heap) == 1:
      return self.heap.pop()

    min_val = self.heap[0]
    self.heap[0] = self.heap.pop()
    self._heapify_down(0)
    return min_val

  def _heapify_down(self, i):
    smallest = i
    left = self._left_child(i)
    right = self._right_child(i)

    if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
      smallest = left
    if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
      smallest = right

    if smallest != i:
      self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
      self._heapify_down(smallest)


# Example usage:
h = MinHeap()
for num in [10, 3, 5, 2, 8]:
  h.insert(num)

print(h.extract_min())  # Output: 2
print(h.extract_min())  # Output: 3

"""3. Self-Balancing Trees: AVL Tree Right Rotation
Question: Implement a Right Rotation function used to rebalance an AVL Tree when a left-heavy imbalance occurs."""
class AVLNode:

  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    self.height = 1


def get_height(node):
  if not node:
    return 0
  return node.height


def right_rotate(y):
  x = y.left
  t2 = x.right

  # Perform rotation
  x.right = y
  y.left = t2

  # Update heights
  y.height = 1 + max(get_height(y.left), get_height(y.right))
  x.height = 1 + max(get_height(x.left), get_height(x.right))

  # Return new root
  return x


# Example setup:
root = AVLNode(30)
root.left = AVLNode(20)
root.left.left = AVLNode(10)

# Perform right rotation to balance
root = right_rotate(root)
print("New root after right rotation:", root.val)  # Output: 20


"""4. Trie (Prefix Tree): Implementation
Question: Implement a Trie class with insert, search, and starts_with methods."""
class TrieNode:

  def __init__(self):
    self.children = {}
    self.is_end_of_word = False


class Trie:

  def __init__(self):
    self.root = TrieNode()

  def insert(self, word):
    curr = self.root
    for char in word:
      if char not in curr.children:
        curr.children[char] = TrieNode()
      curr = curr.children[char]
    curr.is_end_of_word = True

  def search(self, word):
    curr = self.root
    for char in word:
      if char not in curr.children:
        return False
      curr = curr.children[char]
    return curr.is_end_of_word

  def starts_with(self, prefix):
    curr = self.root
    for char in prefix:
      if char not in curr.children:
        return False
      curr = curr.children[char]
    return True


# Example usage:
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))  # Output: True
print(trie.search("app"))  # Output: False
print(trie.starts_with("app"))  # Output: True
