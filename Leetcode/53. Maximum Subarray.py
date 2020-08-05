
"""# 53. Maximum Subarray

+ Compare previous subarray with the new ele, consider negative values

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

'''
Method 1:  brute force  0(n^2)
'''
def maxSubArray(nums):
    sum = 0 
    max_sum = 0
    window_sum = 0
    j = 0     # start indicator
    for i , ele in enumerate(nums):   # window
        sum = 0
        for j in range(i,len(nums)):
            sum += nums[j]
            max_sum = max(max_sum, sum)
            # print ("i,j,sum,max_sum",i,j,sum,max_sum)
    return max_sum

maxSubArray([-2,1,-3,4,-1,2,1,-5,4] )

'''
method 2: Kadane' Algorithm T:0(n) S:0(1)

       0  1  2 3 4  5
       [-2, 1, -3, 4, -1, 2, 1, -5, 4]   sum   max_sum
    0   []                               -2
    1      []                            -1
    2      [    ]                         1    1
        [      ]                         -2    
           [                          -
'''

def maxSubArray(nums):
        import numpy as np
        max_sum = -np.inf
        i = 0     # start indicator
        subarray = []
        sub_sum = 0
        for j , ele in enumerate(nums):          # window_end
            if j == 0 or sub_sum + ele > ele:
                sub_sum += ele
            else:
                sub_sum = ele             
            max_sum = max(max_sum,sub_sum)

            # print (subarray)
        return max_sum


maxSubArray( [1,2,-1,-2,2,1,-2,1,4,-5,4] )