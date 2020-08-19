'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.


Hint:
    1) use "ele-1" to find the smallest value of all sequences 
    2) use "ele+1" to search the consecutive sequence starting from there 
    3) return length
'''

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        """
        len_max = 0
        nums = set(nums)
        
        for i, ele in enumerate(nums):
            if ele - 1 not in nums:                   # find the smallest ele
                temp = ele
                len_temp = 1        

                while temp+1 in nums:    #             # find the consequece
                    len_temp +=1
                    temp += 1
                len_max = max(len_max,len_temp)
        return len_max
            

#%%
A =  [1, 3, 6, 4, 1, 2]
dic = set(A)    # convert to dict/ hash map
miss = list(dic)[-1] +1
for ele in dic:
    if ele-1 not in dic: 
        print ("ele",ele)
        temp = ele
        while temp+1 in dic:
            temp+=1
        print ("temp",temp)        
        miss = min(miss,temp+1)
print ("final",max(miss,1))

# %%
2**2

# %%
