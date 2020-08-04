"""

##Pair with Target Sum (easy)

Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

Example 1:

Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
"""

'''
Time: 0 (N) Space : 0(1)
'''
def pair_with_targetsum(arr, target_sum):
  # TODO: Write your code here
  i = 0
  j = len(arr) -1
  while i<j:
    sum = arr[i] + arr[j]
    if sum > target_sum:  # make it smaller
      j -= 1
    elif sum < target_sum :
      i +=1
    else:
      return [i,j]

  return [-1, -1]