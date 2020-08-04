

"""## Triplet Sum to Zero (medium)

### Problem Statement #
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Example 1:

Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.
"""

'''
Method 1 : # Time(n^3) Space (N)

  0 1 2 3 4 5
0   * * * * *
1     * * * *
2       *
3
4
'''

def search_triplets(arr):
  triplets = []  
  for i in range (len(arr)):        
    for j in range ( len(arr)):
      if j> i : # the top right column of the matrix 
        sum2  = arr[i]+ arr[j]
        temp_arr = arr.copy()                                                   # avoid changing the orgininal arr
        temp_arr[i] = None
        temp_arr[j] = None
        if -sum2 in temp_arr:                                                   # -sum in the remaining temp_arr
          temp_triplet = sorted( [arr[i],arr[j],-sum2 ] )
          if temp_triplet not in triplets:                                      # avoid duplicate
            triplets.append( temp_triplet) 
  return triplets

  # TODO: Write your code here

print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
print(search_triplets([-5, 2, -1, -2, 3]))

'''
Method 2 
Inspired by pair_with_targetsum
 # Time O(n^2), Space O(N)

'''
def pair_with_targetsum(arr, target_i):
  # Time O(n), Space O(N)
  ids = list( range (len(arr)))
  ids.pop(target_i)          # avoid selecting origing 
#   print ("target_i=",target_i,"\t ids=",ids)
  i = 0
  j = len(ids) -1
  target_sum = -arr[target_i]
  triplets = []
  while i<j :
    sum = arr[ids[i]] + arr[ids[j]]
    if sum > target_sum:  # make it smaller
      j -= 1      
    elif sum < target_sum :
      i +=1
    else:  # sum == target_sum
      triplets.append( sorted ( [arr[ids[i]],arr[ids[j]], arr[target_i]]) )     # incase there are more than one pairs sum to target sum
      i +=1
      j -=1
  return triplets

def search_triplets(arr):
  # Time O(n), Space O(N)
  triplets = []  
  arr = sorted (arr)                                                            # Time O(nxlogn)
  for i in  range (len(arr) ):
    if i > 0 and arr[i] == arr[i-1]:                                             # skip same element to avoid duplicate triplets
      continue
    triplets_temp = pair_with_targetsum(arr, i)
    if len(triplets_temp) > 0:
        for triplet in triplets_temp:                                            # avoid duplcate
            if triplet not in triplets:
                triplets.append (triplet)
        
  return triplets

print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
print(search_triplets([-5, 2, -1, -2, 3]))