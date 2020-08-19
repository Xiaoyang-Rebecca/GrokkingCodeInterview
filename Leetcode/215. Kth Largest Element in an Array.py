class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) < k:
            return None
        ls = sorted (nums[:k])   # descending order
        for ele in nums[k:]:
            if ele > ls[0]:
                ls.pop(0)
                ls.append(ele)
                ls = sorted(ls)
        # print (ls)
        return ls[0]
        