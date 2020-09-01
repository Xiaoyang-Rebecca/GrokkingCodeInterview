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
        self.sum = sum
        self.count = 0
        self.currentPath = []
        
        if root == None:
            return self.count                
        
        def checksum(root):            
            if root is not None:                                
                self.currentPath.append(root.val)     
                j = len(self.currentPath) -1
                currentsum = 0
                while j >= 0:                    # exam all the subpath "end" in the root.val
                    currentsum += self.currentPath[j]
                    if currentsum == self.sum :
                        # self.rs .append( list(self.currentPath) )
                        self.count +=1
                    j -=1
                checksum(root.left)
                checksum(root.right)

                self.currentPath.pop(-1)
            
        checksum(root)
        
        return self.count
