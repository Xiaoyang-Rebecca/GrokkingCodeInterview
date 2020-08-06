
'''
Deque: BFS  Time  O(N), Space  O(N)
 # the ony difference between previous problem:
 rather than append to result, insert[0]
'''
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

    result.insert(0,val_ls)                  # the ony difference between previous problem

    print ("result=",result)  

  return result



def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level order traversal: " + str(traverse(root)))


main()
