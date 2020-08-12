'''
Same to "Binary Tree Level Order Traversal (easy).py" ,just take the avg
Space O(n)
Time O(n)
'''

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_level_averages(root):
  result = []
  # TODO: Write your code here
  level_nodes = [root]
  while len(level_nodes)> 0:
    level_width = len (level_nodes)
    val_sum  = 0                                                         #val_ls = []
    for i in range (level_width):
      n = level_nodes.pop(0)
      val_sum+=n.val                                                    #val_ls.append(n.val)

      if n.left is not None:
        level_nodes.append(n.left)
      if n.right is not None:
        level_nodes.append(n.right)
    result.append(val_sum/  level_width)                                #sum(val_ls)/len(val_ls))
  return result

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.left.right = TreeNode(2)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level averages are: " + str(find_level_averages(root)))


main()






