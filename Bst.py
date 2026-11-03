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


