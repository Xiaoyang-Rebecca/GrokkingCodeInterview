Sum of Path Numbers (medium)
Problem Statement
Try it yourself
Solution
Code
Time complexity
Space complexity
Problem Statement #
Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will represent a number. Find the total sum of all the numbers represented by all paths.


class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_sum_of_path_numbers(root):
  # TODO: Write your code here
  if root is None:
    return False
  
  nums = []
  curnum = 0

  def find_next(pt,curnum,nums):
    if pt is not None:
      curnum = curnum*10+ pt.val      
      if pt.left == None and pt.right== None:
        nums.append(curnum)

      find_next(pt.left ,curnum,nums)
      find_next(pt.right,curnum,nums)    

  find_next(root, curnum,nums)
  return sum(nums)



def main():
  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)
  print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
