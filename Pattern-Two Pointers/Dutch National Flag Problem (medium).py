
"""## Dutch National Flag Problem (medium)

Problem Statement #
Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.

The flag of the Netherlands consists of three colors: red, white and blue; and since our input array also consists of three different numbers that is why it is called Dutch National Flag problem.

Example 1:

Input: [1, 0, 2, 1, 0]
Output: [0 0 1 1 2]
"""

''' 
   

'''

def dutch_flag_sort(arr):
  # TODO: Write your code here
  f1,l1 = 0,len(arr) -1                # the id of the first and the last "1" 
  i = 0
  while i <= l1:
    if arr[i] ==1  :
        i +=1
    elif arr[i] == 0:
        arr[i] , arr[f1] = arr[f1] , arr[i]
        f1 +=1
        i +=1
    else:
        arr[i] , arr[l1] = arr[l1] , arr[i]
        l1-=1         
  return arr

def main():
  arr = [1, 0, 2, 1, 0]
  dutch_flag_sort(arr)
  print(dutch_flag_sort(arr))

  arr = [2, 2, 0, 1, 2, 0]
  dutch_flag_sort(arr)
  print(arr)
main()

import numpy as np
a = [[2,6],[1,3],[8,10],[15,18]]
np.sort (a, axis = 0)[0,:]