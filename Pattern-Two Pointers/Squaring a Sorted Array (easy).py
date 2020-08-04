

"""##Squaring a Sorted Array (easy)

Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.

Example 1:

Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]
"""

'''
   Time 0 (n), Space(n)

  # keep in mind that time complexity of insert is o(n), append is o(1)
  # So we can use append and reversed in the end 

   [-2, -1, 0, 2, 3]   abs(i) ? abs(j)
    [             ]         <             [4,9]
    [          ]            >=            [4,4,9]
        [      ]             <            [1,4,4,9]
        [   ]                >            [0,1,4,4,9]

'''
def make_squares(arr):
  squares = []
  # TODO: Write your code here
  i = 0
  j = len(arr) -1
  max_abs = max(abs(arr[i]),abs(arr[j]))
  squares.append (max_abs**2)
  while i<j:
    if abs(arr[i]) < abs(arr[j]):
      squares.append(arr[i]**2)   
      j-=1
    else:
      squares.append(arr[j]**2)
      i+=1

  return squares[::-1]