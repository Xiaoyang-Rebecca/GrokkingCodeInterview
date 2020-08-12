
"""

## Smallest Subarray with a given sum (easy)

### Problem Statement 
Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.

### Example 1:
Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2

Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].
"""

''' Time: O(2N)  Space: O(1)
id     0, 1, 2, 3, 4, 5 
arr    2, 1, 5, 2, 3, 2      sum  min_len  ( required sum >= 7 )
      s,e                     2    &
       s  e                   3    &
       s     e                8    3
          s  e                6    3
          s     e                


'''
def smallest_subarray_with_given_sum(s, arr):
  # TODO: Write your code here
  min_len = len (arr)
  sum_arr = 0
  i_start = 0 
  found= 0

  for i_end, ele in enumerate(arr):
    sum_arr += ele
    '''
        # shrink the window ** "as small as possible" ** until the 'window_sum' is smaller than 's'
    Use while rather than if
    '''
    while sum_arr >= s:
      cur_len = i_end - i_start + 1              # 
      min_len = cur_len if cur_len < min_len else min_len     # save the min_length
      sum_arr -= arr[i_start]
      i_start += 1      # move the i_start right
      found = 1  
  if found == 0:
    return -1
  else:
    return min_len

print ("result=", smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2]) )