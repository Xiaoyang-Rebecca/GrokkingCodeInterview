# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import numpy as np
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return None
        # level_sums = []
        level_sum_max = -np.inf
        ls = [root]
        level = 1
        level_max = None
        while len(ls) > 0:
            l_sum = 0
            len_ls = len(ls)
            for i in range (len_ls):
                n = ls.pop(0)
                l_sum += n.val
                if n.left is not None:
                    ls.append(n.left)
                if n.right is not None:
                    ls. append(n.right)
            if l_sum > level_sum_max:
                level_sum_max = max(l_sum,level_sum_max)
                level_max = level
            level+=1
        return level_max