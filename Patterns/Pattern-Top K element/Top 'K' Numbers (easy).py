
# Method 1 : find largest min_heap Time: O(nlogk)
def find_k_largest_numbers(nums, k):
  # TODO: Write your code here
  ls = sorted(nums[:k])                 # increasing order      # logn
  # make sure the first on is always the smallest
  for ele in nums[k:]:                 
    if ele > ls[0]: 
      ls.pop(0)
      ls.append(ele)
      ls =sorted(ls)                    # logn
  
  return ls


def main():

  print("Here are the top K numbers: " +
        str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

  print("Here are the top K numbers: " +
        str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))


main()

