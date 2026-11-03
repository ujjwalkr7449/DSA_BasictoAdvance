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
