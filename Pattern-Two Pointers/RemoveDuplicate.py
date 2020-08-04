"""### Problem Statement #
Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the new length of the array.

Example 1:

Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
Example 2:

Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].
"""

'''

 [2, 3, 3, 3, 6, 9, 9]         [2]  
     []                j!=j-1  [2, 3]    
     [  ]              j==j-1  [2, 3]    
     [     ]           j==j-1  [2, 3]    
     [        ]        j!=j-1  [2, 3,6]
        [        ]  
  '''
def remove_duplicates(arr):
  # TODO: Write your code here
  i = 1         # move only when the current value is not the same with previous value
  for j in range (1, len(arr)) :   
    if arr[j]!= arr[j-1]:      
      arr[i]=arr[j]
      i+=1
  return i

print (remove_duplicates([2, 3, 6,6, 9,9,10, 10,  100 ]))