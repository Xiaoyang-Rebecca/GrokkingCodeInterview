'''
# if new larger than the current largest, replace it
'''
def find_Kth_smallest_number(nums, k):
  # TODO: Write your code here
  ls = sorted(nums[:k], reverse = True)     # decreasing order
#   print (ls)
  for ele in nums[k:]:
      if ele < ls[0]:                       # the first one always the smallest
            ls.pop(0)
            ls.append(ele)
            ls = sorted(ls,reverse = True)  # decreasing order

  return ls[0]


def main():

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

  # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))


main()
