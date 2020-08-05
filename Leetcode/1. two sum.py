
"""#1. two sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

'''
Method 1: brute force  T:0(N^2), S :0(N)
        id = np.where(num == np.array(list))[0][0]
        
Method 2:   hash table   
        do it only once 

       b values     Target = 9
        i     [2, 7, 11, 15]     nums_loc
        0      7                  {2:0}
        1         2               {2:0, 7:1}

'''
import numpy as np
def twoSum( nums, target):
    nums_loc = {}
    for i, num in enumerate (nums):
        b = target - num 
        if b not in nums_loc :         # hash table, storage the loc of candidate num visited
            nums_loc[num] = i
        else:
            return [ nums_loc[b] ,i  ]
    print (nums_loc)
    return [None, None]

nums = [2, 7, 11, 15]
target = 9
twoSum(nums, target)