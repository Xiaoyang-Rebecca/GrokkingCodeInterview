class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = []
        if len(nums ) ==0:
            return subsets
        subsets. append([])
        for ele in nums:
            level_width = len (subsets)
            for i in range (level_width):
                new_node = list(subsets[i])
                new_node.append(ele)
                subsets.append(new_node)
        return subsets
            