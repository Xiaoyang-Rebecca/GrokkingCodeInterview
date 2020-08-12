class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):
  result = []
  # TODO: Write your code here
  level_nodes =[root]
  while len(level_nodes) > 0:
    leval_width = len(level_nodes)  
    val_ls = []
    for i in range(leval_width):
      n = level_nodes.pop(0)               # current node
      val_ls.append(n.val)
      if n.left is not None:
        level_nodes.append( n.left ) 
      if n.right is not None:
        level_nodes.append( n.right )

    if len(result)% 2 ==0 :              # order l->r
      result.append(val_ls)                # the ony difference between previous problem
    else:
      result.append(val_ls[::-1])          # the ony difference between previous problem

  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.right.left.left = TreeNode(20)
  root.right.left.right = TreeNode(17)
  print("Zigzag traversal: " + str(traverse(root)))


main()
