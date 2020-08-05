
"""## Triplet Sum Close to Target (medium)

### Problem Statement #
Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.

Example 1:

Input: [-2, 0, 1, 2], target=2
Output: 1
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.
"""

import numpy as np
def triplet_sum_close_to_target ( arr, target):
    arr = sorted(arr)               # time : O(nlogn)
    diff_min = np.inf
    target_sum = 0
    for i in range (len (arr) - 1):
        left = i+1
        right = len(arr) - 1
        target_two_sum = target - arr[i]      # make it as close as posible 
        while  left < right:
            # calcualte sum 
            two_sum = arr[left] + arr[right]
            three_sum = arr[i] + arr[left] + arr[right]
            if abs (target -  three_sum ) < diff_min :
                diff_min = min ( diff_min, abs (target - three_sum )  )
                target_sum = three_sum

            # determin the direction of the next step
            if two_sum < target_two_sum:      # increase it !
                left +=1
            else:
                right -=1
    return target_sum

def main():
  print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
  print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
  print(triplet_sum_close_to_target([1, 0, 1, 1], 100))


main()