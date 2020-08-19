


"""#136. Single Number

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""

#

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """    
        i = 0  # pointer for the current element 
        r = []
        # single = nums [0]    
        while  i <len(nums):     
            num = nums[i]
            if num not in r :  # single
                r.append(num)
            else:   # double
                r.remove(num)        
            i+=1
        if len(r)==1 :
            return r[0]
        else:
            return None
