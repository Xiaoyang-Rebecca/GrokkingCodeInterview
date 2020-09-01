"""
Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.
Key: seuqenceid==> sid
"""
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_path(root, sequence):
  # TODO: Write your code here
  if root is None:
    return False

  def check_sequence(root,sequence, sid):
    if root is None:
      return False
      
    if root.left == None and root.right == None  :                  # leaf node
      if  sid == len(sequence)-1 and root.val == sequence[sid]:     # equal
        return True
      else:
        return False

    return check_sequence(root.left,sequence, sid+1) + check_sequence(root.right,sequence, sid+1)   

  return check_sequence(root,sequence,0)  


def main():

  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)

  print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
  print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()
