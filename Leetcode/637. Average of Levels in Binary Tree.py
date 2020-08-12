# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root == None:
            return None
        result = []
        # TODO: Write your code here
        level_nodes = [root]
        while len(level_nodes)> 0:
            level_width = len (level_nodes)
            val_sum  = float(0)                                                         #val_ls = []
            for i in range (level_width):
                n = level_nodes.pop(0)
                val_sum+=n.val                                                    #val_ls.append(n.val)

                if n.left is not None:
                    level_nodes.append(n.left)
                if n.right is not None:
                    level_nodes.append(n.right)
            result.append(val_sum/  level_width)                                #sum(val_ls)/len(val_ls))
        return result
