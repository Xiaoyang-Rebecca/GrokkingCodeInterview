

"""## Longest Subarray with Ones after Replacement (hard)

Problem Statement #
Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

Example 1:

Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.
"""

'''

 [0, 1, 0, 1 ,0]  len(num1) Dict         (num0<=k=2)  
 []                  1      {0:1 ,1:0}     
 [   ]               2      {0:1 ,1:1}
 [      ]            2      {0:2 ,1:1}
 [         ]        

'''
def length_of_longest_substring(arr, k):
  # TODO: Write your code here
  freq = {0:0,1:0}
  i = 0     # starting 
  max_len = 0
  for j , a in enumerate (arr):
    freq[a] +=1
    while freq[0] > k:
      freq[arr[i]] -=1
      i+=1
    max_len = max(max_len, j-i+1)

  return max_len