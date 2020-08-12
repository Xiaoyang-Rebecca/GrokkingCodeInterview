class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_minimum_depth(root):
  # TODO: Write your code here
  min_depth = 0
  ls = [root]
  while len(ls)>0:
    min_depth +=1
    level_width = len (ls)
    for i in range(level_width):
      n = ls.pop(0)
      if n.left ==None and n.right == None:
        return min_depth
      else:
        if n.left is not None:
          ls.append(n.left)
        if n.right is not None:
          ls.append(n.left)
        
  return min_depth


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()
