
'''
Deque: BFS  Time  O(N), Space  O(N)
  n.val leval_width   level_nodes  result
    12    1            [7,1]       [ [12] ]
    7     2            [1,9]
    1     2            [9,10,5]    [ [12],[7, 1]]
    9     3            [10,5]      
    10    3            [5]      
    5     2            []          [[12], [7, 1], [9, 10, 5]]
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

    result.append(val_ls)

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
