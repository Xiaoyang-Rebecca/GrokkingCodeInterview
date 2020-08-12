#90. Subsets II


# method 1

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = []
        subsets.append([])
        for ele in sorted(nums):
            level_width = len (subsets)
            for i in range(level_width):
                new = list(subsets[i])
                new.append(ele)
                if new not in subsets:
                    subsets.append(new)
        return subsets