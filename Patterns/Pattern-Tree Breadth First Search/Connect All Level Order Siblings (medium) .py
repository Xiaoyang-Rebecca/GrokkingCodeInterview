'''
Connect All Level Order Siblings (medium) #
Given a binary tree, connect each node with its level order successor. The last node of each level should point to the first node of the next level.
   1 -
 -2--3-
-4--5--6--7-Null 

'''

from __future__ import print_function
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None

  # tree traversal using 'next' pointer
  def print_tree(self):
    print("Traversal using 'next' pointer: ", end='')
    current = self
    while current:
      print(str(current.val) + " ", end='')
      current = current.next


def connect_all_siblings(root):
  # TODO: Write your code here
  ls = [root]
  while len(ls)>0:
    p = ls.pop(0)
    if p.left is not None:
      ls.append(p.left)
    if p. right is not None:
      ls.append(p.right)
    if len(ls)==0:
      break
    p.next = ls[0]
  return


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  connect_all_siblings(root)
  root.print_tree()


main()
