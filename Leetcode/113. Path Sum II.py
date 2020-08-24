'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
[5,4,11,7]
'''
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.rs = []
        self.currentPath = []
        if root == None:
            return self.rs
        
        def checksum(root,sum):            
            if root is not None:                
                self.currentPath.append(root.val)     
                if root.val == sum and root.left == None and root.right== None:    # leaf
                    self.rs.append(list(self.currentPath))

                checksum(root.left,sum-root.val)
                checksum(root.right,sum-root.val)

                self.currentPath.pop(-1)
            
        checksum(root,sum)
        
        return self.rs
