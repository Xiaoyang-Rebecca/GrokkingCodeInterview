# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return None
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