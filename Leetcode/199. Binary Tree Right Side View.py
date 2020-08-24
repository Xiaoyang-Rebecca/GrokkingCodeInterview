# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rightNodes = []
        if root is None:
            return rightNodes
        # ls = [root]
        levelNodes = [root]
        while len(levelNodes)>0:
            levelWidth = len(levelNodes)
            for i in range(levelWidth):
                currentNode = levelNodes.pop(0)
                if currentNode.left is not None:
                    levelNodes.append(currentNode.left)
                if currentNode.right is not None:
                    levelNodes.append(currentNode.right) 
            rightNodes.append(currentNode.val)                    # the last node in this level
        return rightNodes
                    
                